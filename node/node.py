import socket
from threading import Thread
import time

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(())



def server():
    HOST = socket.gethostname() # ip address to run through eth0 port to docker
    PORT = 80 # desired socket port from docker compose
    # create a new socket using 'with' to avoid having to include 'close()'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) # bind to the socket
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

def client ():
    HOST_CLI = socket.gethostname()
    PORT_CLI = 80 #The port that the server uses
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_CLI, PORT_CLI))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

Thread(target = server).start()

time.sleep(0.5)

Thread(target = client).start()
