import threading
import time
import random
import socket
import sys
import os


def portNum():
    """
    This function pulls the arguments from the cmd line and populates an array with each argument.
    :return: str[]  -   By the structure of this command it should hold, the RSHostName, the RSPort, and TSPort. In
        that order.
    """
    fullargs = sys.argv
    arglist = fullargs
    return arglist


def client():
    # Populates all necessary arguments in an array
    args = portNum()

    # Initializes the Root Server connection
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Binds the RS Port and creates the connection
    rs_port = int(args[2])
    rs_hostname = socket.gethostbyname(socket.gethostname()) # localhost?
    rs_binding = (rs_hostname, rs_port)
    rs.connect(rs_binding)

    # Receive connect confirmation from RS
    rs_connect_conf = rs.recv(100)
    print(rs_connect_conf.decode('utf-8'))

    # Generates the resolved hostname list
    if os.path.exists("RESOLVED.txt"):
        os.remove("RESOLVED.txt")
    resolved_queries = open("RESOLVED.txt", "w")

    # Generates the query list from the text file
    query_list_file = open("PROJI-HNS.txt", "r")
    query_list = query_list_file.readlines()

    for query in query_list:

        # Send Hostname being queried to RS
        hostname = query
        rs.sendall(hostname.encode())
        # Receive response from RS to Client
        rs_query_return = rs.recv(100)
        print("[C] Hostname Query Return: " + rs_query_return)

        # Split query return to check flag
        #
        #

        # Execute based on flag
        # > If A --> Resolved DNS
        # > If NS --> Initialize TS and perform 2nd lookup

    end_flag = "done"
    rs.sendall(end_flag.encode())
    # Initializes the Top-Level Server connection
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Sets the TS Port
    ts_port = int(args[3])
    ts_hostname = socket.gethostbyname(socket.gethostname()) # localhost?
    ts_binding = (ts_hostname, ts_port)
    ts.connect(ts_binding)

    # Receive Connect from the servers
    data_from_server1 = ts.recv(100)
    print("[C]: Data received from server: {}".format('\n' +
                                                      data_from_server1.decode('utf-8')))

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