# EXLAP 1.3 Schema and Python interface


PURPOSE


This project is an API to interface with the EXLAP protocol.


EXLAP BACKGROUND


EXLAP is found in many vehicles produced by the Volkswagon Auto Group (VAG).
Where avaliable, EXLAP allows you access to many different vehicle telemetry
sources such as brake pressure, wheel speed, seatbelt status, steering angle,
and potentially controls such as those found in a vehicle stereo/entertainment
system. This project was tested against EXLAP commands avaliable on specific
models of Porsche vehicles. More commands likely exist in other VAG model
vehicles, and are easily discovered using this project.


EXLAP was seemingly designed as a standardized method for manufactures to
interface with vehicle systems over a common API. VAG attempted to evangalize
adoption of this protocol, but it seems those attempts were unsuccessful and now
abandoned.


Through the EXLAP documentation found from 2017, I was able to release this
project under a Creative Common license.


The longevity of EXLAP is unknown, however it has been used in cars as recent as
2024, and it will remain functional in all cars previously shipped with it, so
continued exploration of this protocol seems worthwhile. I could not identify the
first year EXLAP was shipped, but I would guess it is around 2012 - 2015.


USE


*Credentials* (creds.py) must be provided to speak to EXLAP authenticated commands.


You can find credentials for your model vehicle several ways. Existing apps
that interface with your vehicle have hard coded credentials, the EXLAP server
running in the vehicle likely has unprotected memory or files you can read.


Full demonstration of protocol is limited without authentication. Unauthenticated
it is still possible to test connectivity by issuing the Req_Dir('*') command to
an EXLAP server. This will result in a response showing avaliable commands, but
likely will be very limited.


Modify the main.py file with the ip address and EXLAP commands you wish to issue
the server.


PROJECT INFO


This project required a patch to asyncio, and assumes python 3.10.9 is present.
Likely, it will work on earlier version of python 3. XML schema was pythonified
using https://www.davekuhlman.org/generateDS.html


Main files of interest:
exlap_cmds.py - contains function for exlap commands and auth
exlap_v2.py - DSgenerate of exlap xml schema into python objects
exlapv2_subs.py - flexible python function for exlap cmd
main.py - connects to exlap server and issue commands
streams.py - patch for asyncio python streams


## Project Folder Structure


- **src/**      src code
- **docs/**     project documentation, exlap schema files
- **dep/**      project dependencies such as python patches and imports
- **samples/**  demonstrations of basic project capabilties


Some future idea for this project are better parsing of exlap responses


- Validation of data sources and format ()


- Test access over USB (the protocol says it supports it)


- Test websockets (also documented but unable to establish a connection)




Known Issues:


EXLAP Authentication was not as documented in the schema. MD5 appears no longer
used.


Websockets connection upgrade did not function as documented in schema.
