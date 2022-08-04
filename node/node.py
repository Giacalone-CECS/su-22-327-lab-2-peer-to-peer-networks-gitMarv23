import socket

HOST = '127.0.0.1' # ip address to run through eth0 port to docker
PORT = 80 # desired socket port from docker compose

# create a new socket using 'with' to avoid having to include 'close()'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # bind to the socket (currently in progress)
    s.listen() # listen for any connections
     # accept connection request
     # receive/send loop until communication closure