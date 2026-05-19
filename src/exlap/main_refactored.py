#!/opt/homebrew/bin/python3
"""
Refactored EXLAP client with improved efficiency and error handling.
"""
import sys
import asyncio
import base64
import hashlib
import random
import aiofiles
import logging
from typing import Optional

import exlap_cmds as cmd
import exlap_v2 as api
from lxml import etree
import streams
import creds

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --Global Configuration--
SESSION_START = 98
MAX_SESSION_ID = 999999998


class SessionManager:
    """Thread-safe session ID manager"""
    def __init__(self, start_id: int = SESSION_START):
        self._session_number = start_id
        self._lock = asyncio.Lock()
    
    async def increment(self) -> int:
        async with self._lock:
            if self._session_number <= MAX_SESSION_ID:
                self._session_number += 1
            else:
                self._session_number = 1
            return self._session_number
    
    @property
    def current_id(self) -> int:
        return self._session_number


class EXLAPClient:
    """Async EXLAP TCP client with improved error handling"""
    
    def __init__(self, host: str, port: int, session_manager: SessionManager):
        self.host = host
        self.port = port
        self.session_manager = session_manager
        self.reader = None
        self.writer = None
        self.authenticated = False
        self.nonce = ""
        self._is_connected = False
    
    async def connect(self):
        """Establish connection to EXLAP server"""
        try:
            self.reader, self.writer = await streams.open_connection(self.host, self.port)
            self._is_connected = True
            logger.info(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise
    
    async def send(self, message: str):
        """Send message with proper error handling"""
        if not self._is_connected:
            raise ConnectionError("Not connected to server")
        
        try:
            self.writer.write(message.encode("utf8"))
            await self.writer.drain()
            logger.debug(f"Sent: {message[:100]}...")
            await self._write_to_file('exlap.txt', message)
        except Exception as e:
            logger.error(f"Send failed: {e}")
            raise
    
    async def receive(self) -> Optional[bytes]:
        """Receive message with timeout and error handling"""
        if not self._is_connected:
            raise ConnectionError("Not connected to server")
        
        try:
            data = await asyncio.wait_for(
                self.reader.readuntil([b"</Rsp>", b"</Req>", b"</Dat>", b"</Status>"]),
                timeout=30.0  # 30 second timeout
            )
            await self._write_to_file('exlap.txt', data.decode('utf-8'))
            logger.debug(f"Received: {data.decode('utf8')[:100]}...")
            
            # Auto-parse nonce if not authenticated
            if not self.authenticated and not self.nonce:
                await self._parse_nonce(data)
            
            return data
        except asyncio.TimeoutError:
            logger.warning("Receive timeout")
            return None
        except Exception as e:
            logger.error(f"Receive failed: {e}")
            raise
    
    async def _parse_nonce(self, data: bytes):
        """Parse nonce from server response"""
        try:
            doc = etree.XML(data.decode())
            challenge_elem = doc.find("Challenge")
            if challenge_elem is not None:
                self.nonce = challenge_elem.get("nonce")
                self.authenticated = True
                logger.info("Nonce received, authentication ready")
        except Exception as e:
            logger.warning(f"Could not parse nonce: {e}")
    
    async def _write_to_file(self, filename: str, content: str):
        """Write content to file asynchronously"""
        try:
            async with aiofiles.open(filename, "a") as f:
                await f.write(content + "\n")
        except Exception as e:
            logger.warning(f"File write failed: {e}")
    
    async def close(self):
        """Close connection properly"""
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            self._is_connected = False
            logger.info("Connection closed")


def generate_nonce(length: int = 16) -> bytes:
    """Generate pseudo-random nonce"""
    return bytes([random.randint(0, 255) for _ in range(length)])


def generate_cnonce() -> str:
    """Generate client nonce as base64 encoded string"""
    cnonce_bytes = bytes([random.randint(0, 255) for _ in range(16)])
    return base64.b64encode(cnonce_bytes).decode("utf-8")


def calculate_sha256_digest(user: str, password: str, nonce: str, cnonce: str) -> str:
    """Calculate SHA256 digest for EXLAP authentication"""
    # More efficient string construction
    digest_input = f"{user}:{password}:{nonce}:{cnonce}"
    digest = hashlib.sha256(digest_input.encode("utf-8"))
    return base64.b64encode(digest.digest()).decode("utf-8")


def create_auth_challenge(session_manager: SessionManager) -> str:
    """Create authentication challenge request"""
    message = api.Req()
    message.set_id(session_manager.current_id)
    
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.CHALLENGE)
    auth.set_useHash("sha256")
    message.set_Authenticate(auth)
    
    return str(message)


def create_auth_response(session_manager: SessionManager, nonce: str, 
                        user: str, password: str) -> str:
    """Create authentication response request"""
    message = api.Req()
    message.set_id(session_manager.current_id)
    
    cnonce = generate_cnonce()
    digest = calculate_sha256_digest(user, password, nonce, cnonce)
    
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.RESPONSE)
    auth.set_cnonce(cnonce)
    auth.set_digest(digest)
    auth.set_user(user)
    message.set_Authenticate(auth)
    
    return str(message)


async def authenticate_client(client: EXLAPClient, user: str, password: str) -> bool:
    """Authenticate with EXLAP server with retry logic"""
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            # Wait for initial response
            await client.receive()
            
            # Send auth challenge
            await client.send(create_auth_challenge(client.session_manager))
            await asyncio.sleep(1)
            
            # Wait for challenge response
            await client.receive()
            
            if client.authenticated and client.nonce:
                # Send auth response
                await client.send(
                    create_auth_response(client.session_manager, client.nonce, user, password)
                )
                logger.info("Authentication successful")
                return True
            else:
                logger.warning(f"Attempt {attempt + 1}: Not yet authenticated")
                await asyncio.sleep(retry_delay * (attempt + 1))
                
        except Exception as e:
            logger.error(f"Authentication attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
    
    logger.error("Authentication failed after maximum retries")
    return False


async def heartbeat_task(client: EXLAPClient, interval: float = 2.0):
    """Send heartbeat messages at regular intervals"""
    try:
        while client._is_connected and client.authenticated:
            await asyncio.sleep(interval)
            await client.send(cmd.Req_heartbeat())
    except asyncio.CancelledError:
        logger.info("Heartbeat task cancelled")
    except Exception as e:
        logger.error(f"Heartbeat failed: {e}")


async def exlap_worker(client: EXLAPClient, command_queue: asyncio.Queue):
    """Process commands from queue"""
    logger.info("EXLAP worker started")
    
    try:
        while True:
            task = await command_queue.get()
            try:
                await client.send(task)
                command_queue.task_done()
            except Exception as e:
                logger.error(f"Failed to send command: {e}")
            finally:
                command_queue.task_done()
    except asyncio.CancelledError:
        logger.info("EXLAP worker cancelled")
    except Exception as e:
        logger.error(f"EXLAP worker failed: {e}")


async def main():
    """Main application entry point"""
    # Configuration
    DEBUG_MODE = True
    HOST = "127.0.0.1" if DEBUG_MODE else "10.173.189.1"
    PORT = 8888 if DEBUG_MODE else 25010
    
    # Initialize session manager
    session_manager = SessionManager()
    
    # Create client
    client = EXLAPClient(HOST, PORT, session_manager)
    
    try:
        # Connect
        await client.connect()
        
        # Authenticate
        authenticated = await authenticate_client(client, creds.user, creds.password)
        if not authenticated:
            logger.error("Failed to authenticate, exiting")
            return
        
        # Setup command queue
        command_queue = asyncio.Queue()
        
        # Add commands to queue
        commands = [
            cmd.Sub_lateralAcceleration(),
            cmd.Sub_espTyreVelocities(),
            cmd.Sub_longitudinalAcceleration()
        ]
        
        for command in commands:
            await command_queue.put(command)
        
        # Create worker tasks
        worker_task = asyncio.create_task(exlap_worker(client, command_queue))
        heartbeat_task_obj = asyncio.create_task(heartbeat_task(client))
        
        # Wait for queue to be processed
        await command_queue.join()
        logger.info("All commands processed")
        
        # Keep connection alive
        while True:
            await client.receive()
            
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    except Exception as e:
        logger.error(f"Application error: {e}")
    finally:
        # Cleanup
        worker_task.cancel()
        heartbeat_task_obj.cancel()
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
