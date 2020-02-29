# Dual-Layer-DNS-Server-Project


0. Authors

Alec Rodrigues (aer153)
Jared Montalbo (jvm104)

_________________________________________

1. Overview

The TS and RS server builds their DNS tables in a hash map on the provided 
files (PROJI-DNSRS.txt) and (PROJI-DNSTS.txt). The client first connects to RS, 
iterates through the hosts provided in (PROJ-HNS.txt) and then sends each 
hostname info to RS. RS compares each host recieved to its dns table and see 
if there is a match. If there is a match it sends the entry as a string 
(Hostname IP address A), otherwise it sends an error string (TSHostname - NS).

Once the client recieves back the strings, the success strings are printed in 
RESOLVE.txt and if it detects an NS, then the hostnames are put into an array 
that is to be send to TS. The client then connects to TS and sends the array 
of hostnames that failed to find a match. TS evaluates similarly to RS. It 
checks for a match in the table, if there is a match send the entry as a 
string (Hostname IP address A), otherwise send an error string (Hostname - Error:HOST NOT FOUND)

Once the client recieves back the strings, the success strings and error strings are both printed in RESOLVE.txt.
RESOLVE.txt will have the results of each hostname provided in the (PROJI-HNS.txt).

_________________________________________

2. Known Problems

There are no known issues or functions in the attached code.

_________________________________________

3. Issues in Development

Testing was an issue I had when developing this project. I had to set up some 
specific commands in my IDE before I could start testing properly. Also, 
since we are developing on an older version of Python, some of the information 
I found online didn't apply to my Python version.

_________________________________________

4. What did we Learn?

I learned a lot about the functionality of a recursive DNS system. Actually implementing
the system made me understand more about how the client communicates with different DNS
servers.
