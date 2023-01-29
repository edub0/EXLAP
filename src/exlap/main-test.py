#!/opt/homebrew/bin/python3
import sys

sys.path.append(".")

import asyncio
import base64
import hashlib
import random

import exlap_cmds as cmd
import exlap_v2 as api
from lxml import etree
import streams


# --Global--
# Because VAG starts at 99
session_number = 98
nonce = ""
user = "PHP-D22200"
password = "Gv2g7nOS9DN1bkQA9YFDttZ1QqNeUDzg/2rzrnEKH70="

# netcat debug flag
debug_127 = 1

# Create FIFO queues to store exlap commands
# Exlap authentication commands
exlap_auth = asyncio.Queue()
# Exlap subscription commands submitted after authentication
exlap_queue = asyncio.Queue()

# --/Global--




def make_cnonce():
    """seeds a cnonce, returned as a 16 int byte arrary-> base64 encoded-> and
    converted to a str
    """
    b_cnonce = bytearray(16)
    for i in range(16):
        b_cnonce[i] = random.randint(0, 255)
        cnonce = (base64.b64encode(b_cnonce)).decode("utf-8")
    return cnonce


def Req_Auth_Challenge():
    """
    Step one of two to auth to exlap server

    Initiates Authentication attempt, ie:
    <Req id="100"><Authenticate phase="challenge" useHash="sha256"/></Req>
    """
    # TODO currently using modified XML schema (added 'useHash' to Authenticate branch)
    # using 'api' exlap library which extends exlap.py with additional comamnds to export and new xml schema.
    message = api.Req()
    cmd.conn_count()
    message.set_id(session_number)
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.CHALLENGE)
    auth.set_useHash("sha256")
    # TODO improve XML schema for sha256 support, ie. auth.set_useHash('sha256')
    message.set_Authenticate(auth)
    return str(message)


def Req_Auth_Response(nonce):
    """
    Step two of two to auth to exlap server

    using nonce_worker(), parses response xml msg from server for nonce content.
    nonce_worker passes nonce value to exlap_sha256_64() and creates a sha256
    digest, ie.

    <Req id="101">
        <Authenticate phase="response" cnonce="1Y9BZPOYQyfBMQrqM/cDaA=="
        digest="BBk5/Y2EVXJW1oRQ+Kan0iN/nZTGnHtVGles9a8zCTQ=" user="PHP-D22200"/>
    </Req>

    """
    message = api.Req()
    cmd.conn_count()
    message.set_id(session_number)
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.RESPONSE)
    cnonce = make_cnonce()
    auth.set_cnonce(cnonce)
    digest = exlap_sha256_as_b64(user, password, nonce, cnonce)
    auth.set_digest(digest)
    auth.set_user(user)
    message.set_Authenticate(auth)
    return str(message)


async def nonce_worker(data):
    """
    Worker function which reads msgs on AsyncTCPClient() recieve worker, parsing
    for utilizes it for Req_Auth_Response() msg.
    """
    global nonce
    if nonce == "":
        try:
            doc = etree.XML(data.decode())
            memoryElem = doc.find("Challenge")
            nonce = memoryElem.get("nonce")
            # asyncio.create_task(await client.send(Req_Auth_Response(nonce)),(f'auth-submittal', exlap_queue))
            exlap_queue.put_nowait(await client.send(Req_Auth_Response(nonce)))
        except Exception as e:
            print(
                f"Something broke in nonce_worker - {e}\nLikely server responded without a response msg.\nTODO - if to check for challenge and fail otherwise"
            )
        pass
    else:
        pass


def exlap_sha256_as_b64(user: str, password: str, nonce: bytes, cnonce: bytes):
    """this is a mashup with sha256digest and additional hashing steps required
    for EXLAP auth as implimented. This method is not complient with v1.3 EXLAP
    documentation
    TODO - need to probably chance nonce and cnonce formatting when ingesting
    from XML
    """
    digest = hashlib.sha256()
    digest.update((user + ":" + password + ":" + nonce + ":" + cnonce).encode("utf-8"))
    base64encoded = base64.b64encode(digest.digest()).decode("utf-8")
    return base64encoded


class AsyncTCPClient:
    """
    This code defines a class AsyncTCPClient that has three methods connect, send and receive.
    The connect method is used to create a socket object and connect to a server running on
    the specified host and port. The send method is used to send a message to the server and
    the receive method is used to receive messages from the server. The asyncio.open_connection
    function is used to create a socket object and connect to the server. The await
    self.writer.drain() is used to wait for the transmission of the message to complete. The
     await self.reader.read(1024) is used to block until a message is received from the server.
      The close method close the connection.

    The main function creates an object of the class AsyncTCPClient and runs the connect, send,
    and receive methods in a loop. This code also uses the async/await feature of python and
    can be run with python 3.5+ version.

    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        # calling our patched asyncio streams class
        self.reader, self.writer = await streams.open_connection(self.host, self.port)

    async def send(self, message):
        self.writer.write(message.encode("utf8"))
        await self.writer.drain()
        print(f"\nSent: {message}\n")

    async def receive(self):
        """need to add output of the recieve msg to be logged and validated
        Need multiple seperators https://bugs.python.org/issue37141
        """
        data = await self.reader.readuntil(
            [b"</Rsp>", b"</Req>", b"</Dat>", b"</Status>"]
        )
        print(f"\nReceived: {data.decode('utf8')}\n")
        if nonce == "":
            try:
                await nonce_worker(data)
            except:
                print("nonce challenge not found - unauthenticated or still looking")
            pass


    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()



# TODO - moved out of main to allow for testing, can also use a global
if debug_127 == 0:
    client = AsyncTCPClient("10.173.189.1", 25010)
else:
    client = AsyncTCPClient("127.0.0.1", 8888)


async def waiter(event):
    print("waiting for connection..")
    await event.wait()
    print("... got it!")


async def main():
    # This needs to come up before queue workers
    await client.connect()

    # Exlap Authenticaion
    exlap_auths = [Req_Auth_Challenge()]
    for cmds in exlap_auths:
        await exlap_auth.put(cmds)

    async def exlap_auth_worker(name, queue):
        """worker submits exlap auth commands to server"""
        while True:
            task = await exlap_auth.get()
            await client.send(task)
            exlap_auth.task_done()

    asyncio.create_task(exlap_auth_worker(f"exlap_auth_worker", exlap_auth))

    # /Exlap Authentication

    # Exlap Commands
    exlap_commands = [cmd.Req_Dir("*"), cmd.Sub_espTyreVelocities()]
    for cmds in exlap_commands:
        await exlap_queue.put(cmds)

    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 10 second and set the event.
    await asyncio.sleep(5)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task

    async def exlap_worker(name, exlap_queue):
        """worker submits exlap commands to server"""
        while True:
            # Get a "work item" out of the queue.
            task = await exlap_queue.get()
            # Work on the task
            # print(task)
            await client.send(task)
            # Notify the queue that the "work item" has been processed.
            exlap_queue.task_done()
            # print(f'exlap_worker submitted: \n{task}')

    tasks = []

    for i in range(1):
        await exlap_auth.join()
        task = asyncio.create_task(exlap_worker(f"exlap_worker-{i}", exlap_queue))
        tasks.append(task)

        await exlap_queue.join()

    # Main() loop
    while True:

        await client.receive()
        # await future_main() go here


asyncio.run(main())