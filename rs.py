import threading
import time
import random
import socket
import sys


dict = {}


def lookup(query):
    try:
        ip = dict[query]
        return ip
    except:
        return query


def populateTable():

    dnstablefile = open("PROJI-DNSRS.txt", "r")
    dnstable = dnstablefile.readlines()
    for i in dnstable:
        temp = i.split()
        try:
            dict[temp[0]] = (temp[1] + ' ' + temp[2])
        except:
            dict[temp[0]] = (temp[1])
    return


def portnum():
    fullargs = sys.argv
    arglist = fullargs[1]
    return int(arglist)


def rserver():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: RServer socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    populateTable()
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

    if lookup(dns_query) == dns_query:

        csockid.send()
    else:
        csockid.send(lookup(dns_query))


    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='server', target=rserver)
    t2.start()