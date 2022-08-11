import socket
from threading import Thread
import time
from ping3 import ping
import os

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
        ipaddress =  "172.18.0." + str(x+1)
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
                #Getting the filename size
                Flns = conn.recv(25).decode('utf-8')
                if not Flns:
                    break
                    #converts filesize into int
                Flns = int(Flns, 2)
                #Getting the file name
                fileName = conn.recv(Flns).decode('utf-8')
                #getting the size of a file
                filesize = conn.recv(32).decode('utf-8')
                filesize = int(filesize, 2)
                filewrite = open(fileName, 'wb')
                bytesize = 1024
                while filesize > 0:
                    if filesize < bytesize:
                        bytesize = filesize
                    info = conn.recv(bytesize)
                    filewrite.write(info)
                    filesize = filesize - len(info)

                filewrite.close()
                print("file is received! Thanks")






# client definition for receiving and sending data
def client(client, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((client, port))
        for files in os.listdir("/file"):
            Flns = len(files)
            Flns = bin(Flns)[2:].zfill(25)
            s.send(Flns.encode('utf-8'))
            s.send(files.encode('utf-8'))

            filesize = os.path.getsize("/file/"+ files)
            filesize = bin(filesize)[2:].zfill(32)
            s.send(filesize.encode('utf-8'))

            filesend = open("/file/"+ files, 'rb')

            data = filesend.read()
            s.sendall(data)
            filesend.close()
            print("File is sent")





    #     s.sendall(b"Hello, world") # sending message in bytes
    #     data = s.recv(1024)
    # print(f"Received {data!r}")

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
                # scan file directory
                # sync files if not in sync

end = time.time()                       # end run time calculation
print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system


#our file syn program
