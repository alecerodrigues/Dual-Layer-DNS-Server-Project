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
        return query + ' - NS'


def populateTable():

    dnstablefile = open("PROJI-DNSTS.txt", "r")
    dnstable = dnstablefile.readlines()
    for i in dnstable:
        temp = i.split()
        try:
            dict[temp[0]] = (temp[1] + ' ' + temp[2])
        except:
            dict[temp[0]] = (temp[1])
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


    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='server', target=tserver)
    t2.start()
