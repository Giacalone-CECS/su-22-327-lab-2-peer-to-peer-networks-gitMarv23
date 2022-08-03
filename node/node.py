import socket

HOST = "" # ip address to run through eth0 port to docker
PORT = "80" # desired socket port from docker compose

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a new socket
s.bind() # bind to the socket (currently in progress)
 # listen for any connections
 # accept connection request
 # receive/send loop until communication closure
s.close() # close socket connection