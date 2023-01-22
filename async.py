#!/opt/homebrew/bin/python3

import exlap as api
import asyncio
import random
import base64
import hashlib

#Global
# Because VAG starts at 99 for some reason
session_number = 98
nonce = base64.b64decode('3203oZhpeVSQSrtdcC8wCA==')
cnonce = base64.b64decode('1Y9BZPOYQyfBMQrqM/cDaA==')
#digest = 'digesty'
user = 'PHP-D22200'
password = 'Gv2g7nOS9DN1bkQA9YFDttZ1QqNeUDzg/2rzrnEKH70='
#End Globals

def conn_count():
    '''command counter for exlap requests'''
    global session_number
    if session_number <= 999999998:
        session_number += 1
    else:
        session_number = 1

def generate_nonce(length=16):
    """Generate pseudo-random number."""
    a = ''.join([str(random.randint(0, 255)) for i in range(length)])
    return a.encode('utf-8')

def Req_Capability():
    '''Setup a request message
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
    on capabilities matching the string
    '''
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    dir = api.Dir()
    dir.set_urlPattern(dir_filter)
    message.set_Dir(dir)
    return str(message)

# Build a exlap auth answer function
def Req_Auth_Challenge():
    '''
    Initiates Authentication attempt, ie:
    <Req id="100"><Authenticate phase="challenge" useHash="sha256"/></Req>
    Step one of 2 to authimpor
    '''
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    auth = api.Authenticate()
    auth.set_phase(api.phaseType.CHALLENGE)
    #TODO improve XML schema for sha256 support, ie. auth.set_useHash('sha256')
    message.set_Authenticate(auth)
    return str(message)

def calculate_digest_v2(user: str, password: str, nonce: bytes, cnonce: bytes):
    '''this is a MD5 calculation function. Not tested or likely to be completed yet.'''
    digest = hashlib.md5()
    digest.update((user + ":" + password).encode())
    digest2 = hashlib.md5()
    # digest2.update((byte_array_to_hex_string(nonce) + ":" + byte_array_to_hex_string(cnonce)).encode())
    digest2.update((nonce.hex() + ":" + cnonce.hex()).encode())
    digest3 = hashlib.md5()
    # digest3.update((byte_array_to_hex_string(digest.digest()) + ":" + byte_array_to_hex_string(digest2.digest())).encode())
    digest3.update(((digest.digest().hex()) + ":" + (digest2.digest().hex())).encode())
    return digest3.digest()

# Build a exlap auth challenge function
def Req_Auth_Response():
    '''
    Respond to the challenge nonce, ie.
    <Req id="101"><Authenticate phase="response" cnonce="1Y9BZPOYQyfBMQrqM/cDaA==" digest="BBk5/Y2EVXJW1oRQ+Kan0iN/nZTGnHtVGles9a8zCTQ=" user="PHP-D22200"/></Req>
    '''
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    auth = api.Authenticate()
    auth.set_phase('response')
    auth.set_cnonce('meh')
    auth.set_digest('meh+meh')
    auth.set_user('PHP-D22200')
    message.set_Authenticate(auth)

    response = '<Req id="101"><Authenticate phase="response" cnonce="1Y9BZPOYQyfBMQrqM/cDaA==" digest="BBk5/Y2EVXJW1oRQ+Kan0iN/nZTGnHtVGles9a8zCTQ=" user="PHP-D22200"/></Req>'
    api.parseString(response)
    return str(message)

    #api.Authenticate - line 2439 

def calculate_sha256_digest(user: str, password: str, nonce: bytes, cnonce: bytes):
    '''this is a mashup of a sha256digest, with the additional hashing steps required for EXLAP auth as implimented (ie. not EXLAP v1.3 compliant)
    TODO - need to probably chance nonce and cnonce formatting when ingesting from XML
    '''
    digest = hashlib.sha256()
    digest.update((user + ":" + password + ":" + base64.b64encode(nonce).decode() + ":" + base64.b64encode(cnonce).decode()).encode())
    base64encoded = base64.b64encode(digest.digest())
    return base64encoded

def calculate_cnonce():
    '''seed a cnonce as a bytearrary'''
    cnonce = bytearray(16)
    for i in range(16):
        cnonce[i] = random.randint(0, 255)
    return cnonce 
    # TODO - Determine if we should return this properly formatted for insertion into XML response.
    #ie. print(base64.b64encode(calculate_cnonce()).decode('utf-8')) 

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
class AsyncTCPClient:
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
        print(f"Sent: {message}")

    async def receive(self):
        '''need to add output of the recieve msg to be logged and validated
        Need multiple seperators https://bugs.python.org/issue37141
        '''
        #patched to allow for multiple seperators. #<Req/>, <Rsp/>, <Dat/> and <Status/>
        data = await self.reader.readuntil([b'</Rsp>', b'</Req>', b'</Dat>', b'</Status>'])
        print(f"Received: {data.decode('utf8')}")

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

    # async def auth_exlap(self):
    '''create a auth command, injected into the queue'''

    #async def logger(self):
    '''log results somewhere'''

# Queue Management

# TODO - Need workers function

# async def worker_foo(name, queue):
#     '''this processes a command in the queue'''
#     while True:
#         # Get a "work item" out of the queue.
#         task = await queue.get()
#         # Work on the task
#         print('====')
#         print(task)
#         # Notify the queue that the "work item" has been processed.
    # TODO - lookup this command's exact effect
#         queue.task_done()

#         print(f'{name} has finished {task}')

# TODO - Worker functions:
# - ingest the bootstrap exlap command list
# - Insert the commands into the main() loop to be sent
# - read the command, set a heart beat timer into the queue if its a subscription
# - set a timer function to see how long tasks are taking to be completed
# - create a primary key to log subscriptions somewhere



# TODO - Need a way to assign the worker function to process the queue

#     # Create three worker tasks to process the queue concurrently.
#     tasks = []
#     for i in range(1):
#         task = asyncio.create_task(worker_bar(f'worker-{i}', queue))
#         tasks.append(task)

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

async def main():

    client = AsyncTCPClient('127.0.0.1', 8888)
    #client = AsyncTCPClient('10.173.189.1', 25010)
    await client.connect()

    # Create our list of Exlap commands
    exlap_commands = [
    await client.send(Req_Auth_Challenge()),
    await client.send(Req_Auth_Response()),
    await client.send(Req_Dir('*')),
    await client.send(Req_Capability())
    ]

    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Load commands into asyncio.Queue
    for cmds in exlap_commands:
        queue.put_nowait(cmds)

    #TODO - test out whether this logic is necessary and working
    while queue.empty == True:
        command == ''
    else:
        command = await queue.get()

    #TODO - probably should use a worker to pull commands from the queue, preserve
    #the intent of each function and allow me to do heartbeat updates and so on

    # main loop
    while True:
        command
        await client.receive()
        #await future_main() go here

# Disable to test without calling car
#asyncio.run(main())

print(calculate_sha256_digest(user,password,nonce,cnonce))
print(f'cnonce {cnonce}')
print(f'cnonce {cnonce}')

print(calculate_cnonce())
print(base64.b64encode(calculate_cnonce()).decode('utf-8'))