"""
*A simple socket server and client
An improved version that handles multiple connections simultaneously
A server-client application that functions like a full-fledged socket application, complete with its own custom header and content

"""

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")