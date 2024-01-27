#####################################################################################################
# Description: This program creates an HTTP server using the python socket api. The program
# will create a listening socket bound to '127.0.0.1' or 'localhost' and a random port number > 1023.
# You will then use your web browser to connect to this server and receive data.
# Note that this server could be running on any host within your LAN (as long as there's no firewall that can block it)
# Run this program (http_server.py). Start up your web browser and naviagate to 127.0.0.1:8000.
######################################################################################################

import socket
# as specified in the assignment, port number is greater than 1023
server_port = 8000
# SOCK_STREAM indicates its using TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bound to local host with port
server_socket.bind(('127.0.0.1', server_port))

# given data
data = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# Listen to at most 1 connection at a time
server_socket.listen(1)
print("The server on port %d is listening..." % server_port)

while True:
    # Set up a new connection from the client
    new_socket, address = server_socket.accept()
    print(new_socket) # laddr(local address) raddr(remote address)
    print(address)
    # Receives the request message from the client
    message = new_socket.recv(1024).decode()
    # print as a single string
    print("Received: {}".format(str(message)))
    new_socket.send(data.encode())
    print("Sending>>>>>>>>>>")
    print(data)
    print("<<<<<<<<<<<<<<<<<")
    new_socket.close()