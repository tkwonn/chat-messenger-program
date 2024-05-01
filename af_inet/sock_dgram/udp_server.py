from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
# Note that explicitly assigning port number to the socket.
# When anyone sends a packet to port 12000 at the IP address of the server,
# that packet will be directed to this socket
server_socket.bind(('', server_port))
print("The server is ready to receive")

while True:
    # Read from UDP socket into message, getting client's IP address and port number
    message, client_address = server_socket.recvfrom(2048)
    print(f'Client address: {client_address}')
    
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)

# Suppose that a client application sends a request to a server application at port 80 on a remote server.
# The server responds to the client’s address at
# a port number assigned by the client’s operating system;
# this number is not used directly by the client application,
# but is sent to the server along with the original request.

