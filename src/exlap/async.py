#!/opt/homebrew/bin/python3

import src.exlap.exlap as api
import asyncio
import random
import base64
import hashlib
import src.exlap.exlap_v2 as bpi
from lxml import etree
import src.exlap.exlap_cmds as exlap_cmds

#--Global--
# Because VAG starts at 99
session_number = 98
nonce = ''
user = 'PHP-D22200'
password = 'Gv2g7nOS9DN1bkQA9YFDttZ1QqNeUDzg/2rzrnEKH70='

#netcat debug flag
debug_127 = 0

# Create a queue that we will use to store our "workload".
exlap_queue = asyncio.Queue()
exlap_auth = asyncio.Queue()

#--/Global--



def conn_count():
    '''exlap client message counter included in every client created EXLAP cmd 
    to let you track responses
    '''
    global session_number
    if session_number <= 999999998:
        session_number += 1
    else:
        session_number = 1

#TODO - we may be able to remove this entirely. Not needed
def make_nonce(length=16):
    """Generate pseudo-random number.
    this function isn't required but was useful during testing"""
    a = ''.join([str(random.randint(0, 255)) for i in range(length)])
    return a.encode('utf-8')

def make_cnonce():
    '''seeds a cnonce, returned as a 16 int byte arrary-> base64 encoded-> and 
    converted to a str
    '''
    b_cnonce = bytearray(16)
    for i in range(16):
        b_cnonce[i] = random.randint(0, 255)
        cnonce = (base64.b64encode(b_cnonce)).decode('utf-8')
    return cnonce 

def Req_Capability():
    '''Setup a request capabilities message
    ie. <Req id="99"><Protocol version="1" returnCapabilities="true"/></Req>'''
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    protocol = api.Protocol()
    protocol.set_version(1)
    protocol.set_returnCapabilities(True)
    message.set_Protocol(protocol)
    return str(message)

def Req_Dir(dir_filter):
    '''
    create a Dir command to display avaliable commands.
    use '*' for default behavior. Can also submit a specific string to search
    on capabilities matching the string, ie. 
    '''
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    dir = api.Dir()
    dir.set_urlPattern(dir_filter)
    message.set_Dir(dir)
    return str(message)

#TODO - include or kill?
def calculate_digest_v2(user: str, password: str, nonce: bytes, cnonce: bytes):
    '''
    this is a MD5 calculation function for authentication. Not tested or 
    likely working. MD5 may be implimented in other model cars, but appears to 
    default to sha256 in late model Porsche
    '''
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
    '''
    Step one of two to auth to exlap server

    Initiates Authentication attempt, ie:
    <Req id="100"><Authenticate phase="challenge" useHash="sha256"/></Req>
    '''
    # TODO currently using modified XML schema (added 'useHash' to Authenticate branch)
    # using 'bpi' exlap library which extends exlap.py with additional comamnds to export and new xml schema.
    message = bpi.Req()
    conn_count()
    message.set_id(session_number)
    auth = bpi.Authenticate()
    auth.set_phase(bpi.phaseType.CHALLENGE)
    auth.set_useHash('sha256')
    #TODO improve XML schema for sha256 support, ie. auth.set_useHash('sha256')
    message.set_Authenticate(auth)
    return str(message)

def Req_Auth_Response(nonce):
    '''
    Step two of two to auth to exlap server

    using nonce_worker(), parses response xml msg from server for nonce content.
    nonce_worker passes nonce value to exlap_sha256_64() and creates a sha256 
    digest, ie. 

    <Req id="101">
        <Authenticate phase="response" cnonce="1Y9BZPOYQyfBMQrqM/cDaA==" 
        digest="BBk5/Y2EVXJW1oRQ+Kan0iN/nZTGnHtVGles9a8zCTQ=" user="PHP-D22200"/>
    </Req>

    '''    
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.RESPONSE)
    cnonce = make_cnonce()
    auth.set_cnonce(cnonce)
    digest = exlap_sha256_as_b64(user,password,nonce,cnonce) 
    auth.set_digest(digest)
    auth.set_user(user)
    message.set_Authenticate(auth)
    return str(message)

async def nonce_worker(data):
    '''
    Worker function which reads msgs on AsyncTCPClient() recieve worker, parsing
    for utilizes it for Req_Auth_Response() msg.
    '''
    global nonce
    if nonce == '':
        try:
            doc = etree.XML(data.decode())
            memoryElem = doc.find('Challenge')
            nonce = memoryElem.get('nonce')
            #asyncio.create_task(await client.send(Req_Auth_Response(nonce)),(f'auth-submittal', exlap_queue))
            exlap_queue.put_nowait(await client.send(Req_Auth_Response(nonce)))
        except Exception as e:
            print(f'Something broke in nonce_worker - {e}\nLikely server responded without a response msg.\nTODO - if to check for challenge and fail otherwise' )
        pass
    else:
        pass

def exlap_sha256_as_b64(user: str, password: str, nonce: bytes, cnonce: bytes):
    '''this is a mashup with sha256digest and additional hashing steps required 
    for EXLAP auth as implimented. This method is not complient with v1.3 EXLAP 
    documentation
    TODO - need to probably chance nonce and cnonce formatting when ingesting 
    from XML
    '''
    digest = hashlib.sha256()
    digest.update((user + ":" + password + ":" + nonce + ":" + cnonce).encode('utf-8'))
    base64encoded = base64.b64encode(digest.digest()).decode('utf-8')
    return base64encoded


class AsyncTCPClient:
    '''
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

lol amazing
'''
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def send(self, message):
        self.writer.write(message.encode('utf8'))
        await self.writer.drain()
        print(f"\nSent: {message}\n")

    async def receive(self):
        '''need to add output of the recieve msg to be logged and validated
        Need multiple seperators https://bugs.python.org/issue37141
        '''
        #TODO - Note changes from patching to allow for multiple seperators. #<Req/>, <Rsp/>, <Dat/> and <Status/>
        data = await self.reader.readuntil([b'</Rsp>', b'</Req>', b'</Dat>', b'</Status>'])
        print(f"\nReceived: {data.decode('utf8')}\n")
        if nonce == '':
            try:
                await nonce_worker(data)
            except:
                print('nonce challenge not found - unauthenticated or still looking')
            pass
        
        #TODO - Response Functions
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

    # async def auth_exlap(self):
    '''create a auth command, injected into the queue'''

    #async def logger(self):
    '''log results somewhere'''

#TODO - moved out of main to allow for testing, can also use a global
if debug_127 == 0:
    client = AsyncTCPClient('10.173.189.1', 25010)
else:
    client = AsyncTCPClient('127.0.0.1', 8888)

async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    #This needs to come up before the exlap workers
    await client.connect()


    exlap_auths = [
    Req_Dir('1st cmd'),
    Req_Auth_Challenge()
    ]
    for cmds in exlap_auths:
        await exlap_auth.put(cmds)

    async def exlap_auth_worker(name, queue):
        '''worker submits exlap commands to server'''
        while True:
            # Get a "work item" out of the queue.
            task = await exlap_auth.get()
            # Work on the task
            #print(task)
            await client.send(task)
            # Notify the queue that the "work item" has been processed.
            exlap_auth.task_done()
            #done, pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)

            #print(f'exlap_worker submitted: \n{task}')

    asyncio.create_task(exlap_auth_worker(f'exlap_auth_worker', exlap_auth))
  
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 10 second and set the event.
    await asyncio.sleep(10)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task


    #await exlap_auth.join()

# Queue Management

# TODO - Need workers function

    async def exlap_worker(name, exlap_queue):
        '''worker submits exlap commands to server'''
        while True:
            # Get a "work item" out of the queue.
            task = await exlap_queue.get()
            # Work on the task
            #print(task)
            await client.send(task)
            # Notify the queue that the "work item" has been processed.
            exlap_queue.task_done()
            #print(f'exlap_worker submitted: \n{task}')


# TODO - Worker functions:
# - ingest the bootstrap exlap command list
# - Insert the commands into the main() loop to be sent
# - read the command, set a heart beat timer into the queue if its a subscription
# - set a timer function to see how long tasks are taking to be completed
# - create a primary key to log subscriptions somewhere


# TODO - Need a way to assign the worker function to process the queue
    # Method to create workers for a given queue. tasks[] used for worker management
    tasks = []
    for i in range(1):
        await exlap_auth.join()
        task = asyncio.create_task(exlap_worker(f'exlap_worker-{i}', exlap_queue))
        tasks.append(task)


    # Create our list of Exlap commands
    exlap_commands = [
    Req_Capability(),
    Req_Dir('*'),
    Req_Capability(),
    Req_Dir('*')
    ]

    # Load commands into asyncio.Queue
    for cmds in exlap_commands:
        await exlap_queue.put(cmds)
    #TODO removed the await, and that blocks the queue

    print(tasks)
#     # Wait until the queue is fully processed.
# TODO - lookup this command and its use exactly. This just makes sure all threads from the queue,
# the await jobs, are completed and results ready before continuing.
#     await queue.join()

# TODO - need a way to clean/monitor/manage the workers
#     # Cancel our worker tasks.
#     for task in tasks:
#         task.cancel()
#     # Wait until all worker tasks are cancelled.
# TODO - lookup this command exactly and its use
# how is this different from queue.join()?
#     await asyncio.gather(*tasks, return_exceptions=True)

    # usure about this right now
    #await exlap_queue.join()
  

    # #TODO - test out whether this logic is necessary and working
    # if exlap_queue.empty == True:
    #     command == print('queue empty')
    # else:
    #     command = await exlap_queue.get()
    # #---
    #command = await queue.get()    

    #TODO - probably should use a worker to pull commands from the queue, preserve
    #the intent of each function and allow me to do heartbeat updates and so on



    # main loop
    while True:
        
        await client.receive()
        #await future_main() go here

asyncio.run(main())

