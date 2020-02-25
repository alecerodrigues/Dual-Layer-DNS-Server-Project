import threading
import time
import random
import socket
import sys


dict = {}


def lookup(query):
    """
    This function takes the DNS being queried in the form of a string and checks to see if it has a corresponding value
        in the dictionary hash map
    :param query: str   -   The DNS being looked up
    :return: str    -   The return is either the ip and flag for the corresponding DNS or the query itself to indicate
                    no match
    """
    try:
        ip = dict[query]
        return query + ' ' + ip
    except:
        return 'none'


def populateTable():
    """
    This function populates the DNS table from a text file. ALl table inputs are in one of two string formats:
        1. hostname ip-address flag
        2. hostname - NS-flag
    :return: null
    """
    dnstablefile = open("PROJI-DNSRS.txt", "r")
    dnstable = dnstablefile.readlines()
    temptsHostName = ""
    for i in dnstable:
        temp = i.split()
        # try:
        if temp [1] == '-':
            temptsHostName = temp[0] + " - " + temp[2]
        else:
            dict[temp[0]] = (temp[1] + ' ' + temp[2])

        # except:
        #     temptsHostName = temp[0] + " - " + temp[1]
        #     dict[temp[0]] = (temp[1])
    return temptsHostName


def portnum():
    """
    This function is used to parse the port number argument from the console command.
    :return: int    -   The return is an integer that represents teh port number to bind to the port
    """
    fullargs = sys.argv
    arglist = fullargs[1]
    return int(arglist)


def rserver():
    """
    This function starts the root server and performs the DNS lookups.
    :return: null
    """
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: RServer socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    tsHostName = populateTable()
    print('i am ts: ' + tsHostName)
    server_binding = ('', portnum())
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()

    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    msg = "Connected to RServer"
    csockid.send(msg.encode('utf-8'))

    # receives hostname to be queried
    dns_query = csockid.recv(1024)

##DEBUGGING

    print('Looking up DNS: ' + dns_query)
    print('IP Result: ' + lookup(dns_query))
##

    if lookup(dns_query) == 'none':
        csockid.send(tsHostName)
        print ("1")
    else:
        csockid.send(lookup(dns_query))
        print ("2")

    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='server', target=rserver)
    t2.start()