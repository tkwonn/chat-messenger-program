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
server_socket.bind(('', server_port))

# Listen to at most 1 connection at a time
server_socket.listen(1)
print("The server is ready to receive")

while True:
    # Set up a new connection from the client
    # locates the server process that is waiting to accept a connection
    # on port number 12000.
    # The newly created connection socket is identified by 4-tuple values
    connection_socket, address = server_socket.accept()
    # Receives the request message from the client
    message = connection_socket.recv(1024).decode()
    modified_message = message.upper()
    connection_socket.send(modified_message.encode())
    connection_socket.close()

