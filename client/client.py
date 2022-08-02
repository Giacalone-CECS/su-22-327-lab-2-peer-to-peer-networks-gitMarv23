# echo-client.py
import socket
from ftplib import FTP #ftp client

HOST = socket.gethostbyname("server") # The server's hostname or IP address
TCP_PORT = 65432  # The port used by the server
FTP_PORT = 21 # standard for for FTP communications

print(f"Server IP address {HOST}")

# with statement avoids having to call s.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, TCP_PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print(f"Received {data!r}")

# ftp class instance creation
with FTP() as ftp:
    True