import socket
from threading import Thread
import time

def server():
    HOST = '127.0.0.1' # ip address to run through eth0 port to docker
    PORT = 80 # desired socket port from docker compose

    # create a new socket using 'with' to avoid having to include 'close()'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) # bind to the socket (currently in progress)
        print('listening for connections')
        s.listen() # listen for any connections
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                # accept connection request
         # receive/send loop until communication closure




def client ():
    Host = "127.0.0.1"
    Port = 80 #The port that the server uses

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, Port))
        s.sendall(f"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

Thread(target = server).start()
time.sleep(0.5)
Thread(target = client).start()



