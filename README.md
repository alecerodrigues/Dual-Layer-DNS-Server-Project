# Dual-Layer-DNS-Server-Project



0. Authors

Alec Rodrigues (aer153)
Jared Montalbo (jvm104)

_________________________________________

1. Overview

The TS and RS server builds their DNS tables in a hash map on the provided files (PROJI-DNSRS.txt) and (PROJI-DNSTS.txt). The client first connects to RS, iterates through the hosts provided in (PROJ-HNS.txt) and then sends each hostname info to RS. RS compares each host recieved to its dns table and see if there is a match. If there is a match it sends the entry as a string (Hostname IP address A), otherwise it sends an error string (TSHostname - NS).

Once the client recieves back the strings, the success strings are printed in RESOLVE.txt and if it detects an NS, then the hostnames are put into an array that is to be send to TS. The client then connects to TS and sends the array of hostnames that failed to find a match. TS evaluates similarly to RS. It checks for a match in the table, if there is a match send the entry as a string (Hostname IP address A), otherwise send an error string (Hostname - Error:HOST NOT FOUND)

Once the client recieves back the strings, the success strings and error strings are both printed in RESOLVE.txt.
RESOLVE.txt will have the results of each hostname provided in the (PROJI-HNS.txt).

_________________________________________

2. Known Problems

There are no known issues or functions in the attached code. The only way to cause an issue is by not inputting values corrently. Swapping the Root server and Top-Level server port may crash the client. It is also necessary to include the TS hostname in the RS DNS table, otherwise the client will crash attempting to connect to an empty hostname.

_________________________________________

3. Issues in Development

Testing was an issue we had when developing this project. We had to set up some specific commands in our IDEs before we could start testing properly. Also, since we are developing on an older version of Python, some of the information we found online didn't apply to our Python version. Learning/testing Python sockets was also a little bit of a challenge as well, due to some of the restrictions on the Rutgers networks. We found that we were not able to communicate with rs.py and ts.py hosted on one desktop and running the client from a laptop. In order connect and test the sockets, we had to create a mobile hotspot on a cellular device and connect the laptop and desktop to it. From there we experienced no issues in testing and was able to successfully communicate between devices.

_________________________________________

4. What did we Learn?

Due to our unfamliarity with Python sockets, we had to quickly learn and adapt our code to create functional connections. We learned a lot about the functionality of a recursive DNS system. Actually implementing the system made us understand more about how the client communicates with different DNS servers. 
