import threading
import time
import random
import socket
import sys

dict = {}


def lookup(query):

    try:
        ip = dict[query.lower()]
        return query + ' ' + ip
    except:
        return 'none'


def populateTable():

    dnstablefile = open("PROJI-DNSTS.txt", "r")
    dnstable = dnstablefile.readlines()

    for i in dnstable:
        temp = i.split()

        dict[temp[0].lower()] = (temp[1] + ' ' + temp[2])
    return


def portNum():

    fullargs = sys.argv
    arglist = fullargs[1]
    return int(arglist)


def tserver():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: TServer socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    populateTable()
    server_binding = ('', portNum())
    ss.bind(server_binding)
    ss.listen(1)

    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    ##print(lookup('bleh'))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    csockid, addr = ss.accept()

    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    msg = "Connected to TServer"
    csockid.send(msg.encode('utf-8'))
    print(dict)

    dns_query = str(csockid.recv(1024)).rstrip()
    while dns_query != 'done':
        # receives hostname to be queried
        print('Looking up DNS: ' + dns_query)
        print('IP Result: ' + lookup(dns_query))

        if lookup(dns_query) == 'none':
            csockid.send(dns_query + ' - Error:HOST NOT FOUND')
            print ("1") ###DEBUGGING
        else:
            csockid.send(lookup(dns_query))
            print ("2") ###DEBUGGING

        dns_query = str(csockid.recv(1024)).rstrip()

    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='server', target=tserver)
    t2.start()
