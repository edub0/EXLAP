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
import creds


# --Global--
# Because VAG starts at 99
session_number = 98
nonce = ""
user = creds.user
password = creds.password
authd = None
# netcat debug flag
debug_127 = 1
# --/Global--


# TODO - we may be able to remove this entirely. Not needed
def make_nonce(length=16):
    """Generate pseudo-random number.
    this function isn't required but was useful during testing"""
    a = "".join([str(random.randint(0, 255)) for i in range(length)])
    return a.encode("utf-8")


def make_cnonce():
    """seeds a cnonce, returned as a 16 int byte arrary-> base64 encoded-> and
    converted to a str
    """
    b_cnonce = bytearray(16)
    for i in range(16):
        b_cnonce[i] = random.randint(0, 255)
        cnonce = (base64.b64encode(b_cnonce)).decode("utf-8")
    return cnonce
    
    







# TODO - include or kill?
def calculate_digest_v2(user: str, password: str, nonce: bytes, cnonce: bytes):
    """
    this is a MD5 calculation function for authentication. Not tested or
    likely working. MD5 may be implimented in other model cars, but appears to
    default to sha256 in late model Porsche
    """
    digest = hashlib.md5()
    digest.update((user + ":" + password).encode())
    digest2 = hashlib.md5()
    # digest2.update((byte_array_to_hex_string(nonce) + ":" + byte_array_to_hex_string(cnonce)).encode())
    digest2.update((nonce.hex() + ":" + cnonce.hex()).encode())
    digest3 = hashlib.md5()
    # digest3.update((byte_array_to_hex_string(digest.digest()) + ":" + byte_array_to_hex_string(digest2.digest())).encode())
    digest3.update(((digest.digest().hex()) + ":" + (digest2.digest().hex())).encode())
    return digest3.digest()


def Req_Auth_Challenge():
    """
    Step 1 of 2, exlap server authentication
    
    <Req id="100">
    <Authenticate phase="challenge" useHash="sha256"/>
    </Req>
    """
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
    Step 2 of 2, exlap server authentication

    using nonce_worker(), parses response xml msg from server for nonce content.
    nonce_worker passes nonce value to exlap_sha256_64() and creates a sha256
    digest.

    <Req id="101">
        <Authenticate phase="response" cnonce="1Y9BZPOYQyfBMQrqM/cDaA=="
        digest="BBk5/Y2EVXJW1oRQ+Kan0iN/nZTGnHtVGles9a8zCTQ=" user="foobar"/>
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
    Reads msgs on AsyncTCPClient() recieve socket. Parse for challenge nonce.
    Sets nonce AND authd global variables.
    """
    global nonce, authd
    if nonce == "":
        try:
            doc = etree.XML(data.decode())
            memoryElem = doc.find("Challenge")
            nonce = memoryElem.get("nonce")
            authd = True
        except Exception as e:
            print(
                f"EXLAP Server response does not include Challenge - {e}\nResponse: {doc}"
            )
        pass
    else:
        pass


def exlap_sha256_as_b64(user: str, password: str, nonce: bytes, cnonce: bytes):
    """sha256digest and additional hashing steps required for EXLAP auth as implimented. 
    This method is not complient with v1.3 EXLAP documentation from 2017.
    """
    digest = hashlib.sha256()
    digest.update((user + ":" + password + ":" + nonce + ":" + cnonce).encode("utf-8"))
    base64encoded = base64.b64encode(digest.digest()).decode("utf-8")
    return base64encoded



class AsyncTCPClient:
    """
    Asyncio socket connection. Creates three methods connect, send and receive.

    "await self.writer.drain()" waits for completion of msg transmission.

    "await self.reader.readuntil([b"</Rsp>", b"</Req>", b"</Dat>", b"</Status>"]"
    is patched streams.py from asyncio. It chunks data based on lines ending in 
    exlap message tags. patch* https://github.com/python/cpython/pull/16429
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
        """parses recieved messages from tcp socket. Looks for exlap xml tags,
        </Rsp>, </Req>, </Dat>, or </Status>.
        """
        data = await self.reader.readuntil(
            [b"</Rsp>", b"</Req>", b"</Dat>", b"</Status>"]
        )
        if nonce == "":
            try:
                await nonce_worker(data)
            except:
                print("nonce challenge not found - unauthenticated or still looking")
        print(f"\nReceived: {data.decode('utf8')}\n")
        # TODO - Response Functions
        # Setup a response parser (use a worker after the recieve queue is cleared?)
        # Setup response content handling, use below java for error inspiration
        #     public final void setResponseStatus(String str) {
        # if (str == null) {
        #     this.status = 0;
        # } else if (str.equals(ExlapML.STATUS_MSG_OK)) {
        #     this.status = 0;
        # } else if (str.equals(ExlapML.STATUS_MSG_ERROR)) {
        #     this.status = 1;
        # } else if (str.equals(ExlapML.STATUS_MSG_NOTIMPLEMENTED)) {
        #     this.status = 2;
        # } else if (str.equals(ExlapML.STATUS_MSG_SUBSCRIPTIONLIMIT_REACHED)) {
        #     this.status = 3;
        # } else if (str.equals(ExlapML.STATUS_MSG_NOMATCHINGURL)) {
        #     this.status = 4;
        # } else if (str.equals(ExlapML.STATUS_MSG_VERSIONNOTSUPPORTED)) {
        #     this.status = 5;
        # } else if (str.equals(ExlapML.STATUS_MSG_AUTHENTICATIONFAILED)) {
        #     this.status = 6;
        # } else if (str.equals(ExlapML.STATUS_MSG_SYNTAXERROR)) {
        #     this.status = 8;
        # } else if (str.equals(ExlapML.STATUS_MSG_INTERNALERROR)) {
        #     this.status = 9;
        # } else if (str.equals(ExlapML.STATUS_MSG_ACCESSVIOLATION)) {
        #     this.status = 10;
        # } else if (str.equals(ExlapML.STATUS_MSG_INVALIDPARAMATER)) {
        #     this.status = 11;
        # } else if (str.equals(ExlapML.STATUS_MSG_PROCESSING)) {
        #     this.status = 12;
        # } else if (str.equals(ExlapML.STATUS_MSG_NOSUBSCRIPTION)) {
        #     this.status = 1;
        # } else {
        #     throw new IllegalArgumentException("Illegal response status: " + str);
        # }
        # Setup

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()


async def main():

    # TODO localhost for testing via netcat
    if debug_127 == 0:
        client = AsyncTCPClient("10.173.189.1", 25010)
    else:
        client = AsyncTCPClient("127.0.0.1", 8888)

    await client.connect()

    exlap_queue = asyncio.Queue()
    
    # Exlap Authentication
    async def exlap_auth_worker():
        """worker submits exlap auth commands to server
        TODO - this can be made much more robust"""
        global authd, nonce
        while not authd:
            # Read initial server response
            await client.receive()
            # Send auth challenge
            await client.send(Req_Auth_Challenge())
            await asyncio.sleep(2)
            # Read response
            await client.receive()
            print('waiting for connection...<auth_worker>')
        await client.send(Req_Auth_Response(nonce))
        print('Connected! <auth_worker>')

    await exlap_auth_worker()
    # /Exlap Authentication

#### Exlap Commands ####
#### this section is where you add the commands you want to subscribe ####
    exlap_commands = [
        cmd.Sub_espTyreVelocities(),
        cmd.Sub_suspensionStates(),
        cmd.Req_heartbeat(),
        cmd.Sub_gearboxOilTemperature(),
        cmd.Sub_oilTemperature(),
        cmd.Sub_currentGear(),
        cmd.Sub_espTyreVelocities()
        ]
    for cmds in exlap_commands:
        await exlap_queue.put(cmds)


    async def exlap_worker(name, exlap_queue):
        """worker submits exlap commands to server"""
        print('exlap worker check in')
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
        task = asyncio.create_task(exlap_worker(f"exlap_worker-{i}", exlap_queue))
        tasks.append(task)

        await exlap_queue.join()

    async def heartbeat():
        """sends a hearbeat command to exlap server every 2 sec."""
        while client and authd:
            await asyncio.sleep(2)
            await client.send(cmd.Req_heartbeat())
        else:  
            await task.cancel()

    asyncio.create_task(heartbeat())



    # TODO - Worker functions:
    # - ingest the bootstrap exlap command list
    # - Insert the commands into the main() loop to be sent
    # - read the command, set a heart beat timer into the queue if its a subscription
    # - set a timer function to see how long tasks are taking to be completed
    # - og subscriptions somewhere

    # TODO - Need a way to assign the worker function to process the queue
    # Method to create workers for a given queue. tasks[] used for worker management
    #     # Wait until the queue is fully processed.

    # TODO - need a way to clean/monitor/manage the workers
    #     # Cancel our worker tasks.
    #     for task in tasks:
    #         task.cancel()
    #     # Wait until all worker tasks are cancelled.


    # #TODO - test out whether this logic is necessary and working

    while True:
        #print('main True loop')
        await client.receive()
        # await future_main() go here

asyncio.run(main())