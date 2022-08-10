import socket
from threading import Thread
import time
from ping3 import ping

HOST_SRV = socket.gethostname()             # ip address to run through eth0 port to docker
HOST_CLI = socket.gethostbyname(HOST_SRV)   # get host name of other machines on the network
PORT = 80                                   # desired socket port for container
PORT_START = 30000                          # start port number for scanning
PORT_END = 60000                            # end number for port scanning
ip_address = []
m =""

# get total number of nodes in our system
f = open('./totalNodes.txt', mode='r')
totalNodes = int(f.read())       # pull total number of nodes
f.close()
# for port in range(PORT_START, (PORT_END + 1)):
# # #     if port_scan(port,m):
# # #         print(f'port {port,m} is open') # if found print on system

start = time.time() # start calculating run time
for x in range(1, (totalNodes + 1)):
    ipaddress = "192.168.240." + str(x)
    print(ipaddress)
    if ping(ipaddress):
        ip_address.append(ipaddress)
        try:
            for x in ip_address:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((m,PORT))
            print("success")
        except:
            print("failed!")
end = time.time()                       # end run time calculation
print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system

# def port_scan(port,m):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # new socket for scanning
#     try:
#         s.connect((m, PORT))                         # if socket connects return true
#         return True
#     except:
#         return False

# start = time.time() # start calculating run time
#
# # dictate port scanning based on the normal output from docker compose (ports 30,000 -> 60,000)
# for port in range(PORT_START, (PORT_END + 1)):
#     if port_scan(port,m):
#         print(f'port {port,m} is open') # if found print on system
#
# end = time.time()                       # end run time calculation
# print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system

# for m in ip_address:
#     # print(port_scan(PORT,m))
#     # for port in range(PORT_START, (PORT_END + 1)):
#     if port_scan(PORT,m):
#         print(f'port {PORT,m} is open') # if found print on system

# def myping(ip):
#     for x in range(1,(totalNodes + 1)):
#         ipaddress =  "192.168.240." + str(x)
#         if ping(ipaddress) == True:
#             ip_address.append(ipaddress)
#         else:
#             return False

# start = time.time() # start calculating run time
#
# # # dictate port scanning based on the normal output from docker compose (ports 30,000 -> 60,000)
# # for port in range(PORT_START, (PORT_END + 1)):
# #     if port_scan(port,m):
# #         print(f'port {port,m} is open') # if found print on system
#
# end = time.time()                       # end run time calculation
# print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system



def server(HOST_SRV, PORT):
    # create a new socket using 'with' to avoid having to include 'close()'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST_SRV, PORT))            # bind to the socket
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
def client(HOST_CLI, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_CLI, PORT))
        s.sendall(b"Hello, world") # sending message in bytes
        data = s.recv(1024)
    print(f"Received {data!r}")

Thread(target = server, args=(HOST_SRV, PORT)).start()

time.sleep(0.5)

Thread(target = client, args=(HOST_CLI, PORT)).start()

# port scanning the network for available servers
# def port_scan(port,m):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # new socket for scanning
#     try:
#         s.connect((m, PORT))                         # if socket connets return true
#         return True
#     except:
#         return False

# start = time.time() # start calculating run time
#
# # dictate port scanning based on the normal output from docker compose (ports 30,000 -> 60,000)
# for port in range(PORT_START, (PORT_END + 1)):
#     if port_scan(port):
#         print(f'port {port} is open') # if found print on system
#
# end = time.time()                       # end run time calculation
# print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system