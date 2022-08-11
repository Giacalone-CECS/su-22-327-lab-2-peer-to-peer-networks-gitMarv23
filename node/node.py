import socket
from threading import Thread
import time
from ping3 import ping

HOST_SRV = socket.gethostname()             # ip address to run through eth0 port to docker
HOST_CLI = socket.gethostbyname(HOST_SRV)   # get host name of other machines on the network
PORT = 80                                   # desired socket port for container
PORT_START = 20000                          # start port number for scanning
PORT_END = 60000                            # end number for port scanning
ip_address = []                             # list of available ips

# get total number of nodes in our system
f = open('./totalNodes.txt', mode='r')  # open corresponding file
totalNodes = int(f.read())              # pull total number of nodes
f.close()                               # close file to prevent leak

# pings for an ip on the network and appends the list if found
def myping():
    for x in range(1, (totalNodes+1)):
        ipaddress =  "172.20.0." + str(x+1)
        if ping(ipaddress):
            ip_address.append(ipaddress) # add ip to the list

def server(host, port):
    # create a new socket using 'with' to avoid having to include 'close()'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))                # bind to the socket
        print('listening for connections')
        s.listen()                          # listen for any connections
        conn, addr = s.accept()             # accept connection request
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

# client definition for receiving and sending data
def client(client, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((client, port))
        s.sendall(b"Hello, world") # sending message in bytes
        data = s.recv(1024)
    print(f"Received {data!r}")

# port scanning the network for available servers
def port_scan(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:   # new socket for scanning
        s.connect((ip, port))
        print('connection established')                           # if socket connets print message

start = time.time() # start calculating run time

Thread(target = server, args=(HOST_SRV, PORT)).start() # start server thread
time.sleep(0.5)                                        # give a little break
Thread(target = client, args=(HOST_CLI, PORT)).start() # start client thread

myping() # ip address assignment

# dictate port scanning based on the normal output from docker compose (ports 20,000 -> 60,000)
for i in range(0, len(ip_address)):                                  # scan through our list of ip addresses
    for j in range(PORT_START, (PORT_END + 1)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create new socket
            result = s.connect_ex((ip_address[i], j))                # error return if found
            if result == 0:
                print(f"Port {j} is open")

end = time.time()                       # end run time calculation
print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system