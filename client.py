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
    resolved_queries = open("RESOLVED.txt", "a")

    # Generates the query list from the text file
    query_list_file = open("PROJI-HNS.txt", "r")
    query_list = query_list_file.readlines()

    # Get honstname and query list to pass to TNS
    ts_query_list = []
    ts_hostname = ''

    for query in query_list:

        # Send Hostname being queried to RS
        hostname = query
        rs.sendall(hostname.encode())
        # Receive response from RS to Client
        rs_query_return = rs.recv(100)
        print("[C] Hostname Query Return: " + rs_query_return)

        # Split query return to check flag
        split_rs = rs_query_return.split()
        if split_rs[2] == 'A':
            resolved_queries.write(rs_query_return + '\n')

        # Execute based on flag
        # > If A --> Resolved DNS
        # > If NS --> Initialize TS and perform 2nd lookup
        if split_rs[2] == 'NS':
            ts_query_list.append(hostname)
            ts_hostname = split_rs[0]

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
    #ts_hostname = socket.gethostbyname(socket.gethostname()) # Used for testing
    
    ts_binding = (ts_hostname, ts_port)
    ts.connect(ts_binding)

    # Receive Connect from the servers
    ts_connect_conf = ts.recv(100)
    print(ts_connect_conf.decode('utf-8'))

    for query in ts_query_list:

        # Send Hostname being queried to TS
        hostname = query
        ts.sendall(hostname.encode())
        # Recieve Response from RS to Client
        ts_query_return = ts.recv(100)
        print("[C] Hostname Query Return: " + ts_query_return)
        
        resolved_queries.write(ts_query_return + '\n')

    ts.sendall(end_flag.encode())

    # close the client socket
    rs.close()
    ts.close()
    exit()

if __name__ == "__main__":

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")