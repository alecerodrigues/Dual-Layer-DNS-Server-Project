import threading
import time
import random
import socket
import sys


def portNum():
    fullargs = sys.argv
    arglist = fullargs
    return arglist


def client():
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    args = portNum()

    # Define the port on which you want to connect to the server
    port1 = int(args[3])
    localhost_addr1 = socket.gethostbyname(socket.gethostname())
    port2 = int(args[2])
    localhost_addr2 = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding1 = (localhost_addr1, port1)
    server_binding2 = (localhost_addr2, port2)
    ts.connect(server_binding1)
    rs.connect(server_binding2)

    # Receive Connect from the servers
    data_from_server1 = ts.recv(100)
    data_from_server2 = rs.recv(100)
    print("[C]: Data received from server: {}".format('\n' +
                                                      data_from_server1.decode('utf-8') +
                                                      '\n' +
                                                      data_from_server2.decode('utf-8')))

    # Send Host Name to RS
    hostname = args[1]
    rs.sendall(hostname.encode())

    # close the client socket
    ts.close()
    rs.close()
    #exit()

if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")