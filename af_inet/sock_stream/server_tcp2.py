# ######################################################
# Note:
# server process must first be running
# allows server to talk with multiple clients
# source port numbers used to distinguish clients
# ######################################################
from socket import *

server_port = 12000
# create TCP socket for server
server_socket = socket(AF_INET, SOCK_STREAM)
# '': any available network interface
server_socket.bind(('', server_port))

# Listen to at most 1 connection at a time
server_socket.listen(1)
print("The server is ready to receive")

try:
    while True:
        # The newly created connection socket is identified by 4-tuple values
        conn, addr = server_socket.accept()
        # Receives the request message from the client
        message = conn.recv(1024).decode()
        modified_message = message.upper()
        conn.send(modified_message.encode())
        conn.close()
except KeyboardInterrupt:
    print("Shutting down the server")
    server_socket.close()

