#####################################################################################################
# Description: This program creates an HTTP server using the python socket api. 
# The program will create a listening socket bound to '127.0.0.1' or 'localhost' and a random port number > 1023.
# You will then use your web browser to connect to this server and receive data.
# Note that this server could be running on any host within your LAN (as long as there's no firewall that can block it)
# Run this program (http_server.py). Start up your web browser and naviagate to 127.0.0.1:8000.
######################################################################################################

import socket

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
print(f"The server on port {server_port} is listening...")

try:
    while True:
        # Set up a new connection from the client
        conn, address = server_socket.accept()
        print(conn) # laddr(local address) raddr(remote address)
        print(address)
        # Receives the request message from the client
        message = conn.recv(1024).decode()
        # print as a single string
        print(f"Received: {str(message)}")
        conn.send(data.encode())
        print("Sending>>>>>>>>>>")
        print(data)
        print("<<<<<<<<<<<<<<<<<")
        conn.close()
except KeyboardInterrupt:
    print("Shutting down the server")
    server_socket.close()

# Note:
# If you only close the connection conn and not the server_socket, the server will stop communicating with the current client but will still be able to accept new connections from other clients.
# If you don't close the server_socket when it's no longer needed, it will remain open, consuming system resources. In some cases, this could lead to resource leakage, which could degrade system performance over time.