import socket
from threading import Thread
import time

HOST_SRV = socket.gethostname() # ip address to run through eth0 port to docker
HOST_CLI = socket.gethostname() # get host name of other machines on the network
PORT = 80 # desired socket port from docker compose
PORT_START = 30000 # start port number for scanning
PORT_END = 60000 # end number for port scanning

def server(host_srv, port):
    # create a new socket using 'with' to avoid having to include 'close()'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host_srv, port)) # bind to the socket
        print('listening for connections')
        s.listen() # listen for any connections
        conn, addr = s.accept() # accept connection request
        with conn:
            print(f"Connected by {addr}")
            # receive/send loop until communication closure
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def client(host_cli, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_cli, port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

Thread(target = server(HOST_SRV, PORT)).start()

time.sleep(0.5)

Thread(target = client(HOST_CLI, PORT)).start()
'''
# port scanning the network for available servers
def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # new socket for scanning
    try:
        s.connect(()) # if socket connets return true
        return True
    except:
        return False

start = time.time() # start calculating run time

# dictate port scanning based on the normal output from docker compose (ports 30,000 -> 60,000)
for port in range(PORT_START, PORT_END + 1):
    if port_scan(port):
        print(f'port {port} is open') # if found print on system
    else:
        print(f'port {port} is closed') # if not found print notice

end = time.time() # end run time calculation
print(f'Elapse Time: {end-start:.2f}s') # print the elapsed time for our system'''