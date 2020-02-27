# Dual-Layer-DNS-Server-Project

-------- Overview --------  

The goal of this project is to implement a simplified DNS system consisting of a client program and two server programs: RS (a simplified root DNS server) and TS (a simplified top-level DNS server).

-------- Instructions for Use --------

Run program with the following arguements in subsequent terminal windows:

python ts.py [Port#1]

python rs.py [Port#2]

python client.py [rs Hostname] [Port#2] [Port#1] 


Port#1 --> The port the root server will use to communicate with the client.

Port#2 --> The port the top-level server will use to communicate with the client.

rs Hostname --> The hostname of the device running the root server.

*****NETWORK FUNCTIONALITY WORKS FOR DEVICES ON THE SAME NETWORK, TO REFERENCE SELF USE localhost*****

-------- How to configure --------

Root server populates DNS table from PROJI-DNSRS.txt in format:

[Hostname] [IP Address] [Flag (A/NS)]

It also includes:

[ts Hostname] - [NS]

Top-Level server populates DNS table from PROJI-DNSTS.txt in format:

[Hostname] [IP Address] [Flag (A/NS)]
