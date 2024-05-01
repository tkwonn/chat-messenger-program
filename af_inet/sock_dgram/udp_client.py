# ######################################################
# Note:
#  we are not specifying the port number of the client socket,
#  instead letting the os do this for us. This is because the transport layer
#  automatically assigns a port number to the socket
#  (ranging 1024 to 65535 that is currently not being used by any other UDP port in the host)
#  We can add a line after we create the socket to associate a specific port number
#  via bind() method like this, client_socket.bind(('', 15000))
#  UDP socket is fully identified by a two-tuple consisting of
#  a destination IP address and a destination port number.
# ######################################################

import socket

server_name = socket.gethostbyname(socket.gethostname())
print(server_name)
server_port = 12000
# create UDP socket for server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence: ')

# convert string type to byte types with encode() method
# attach sender name, port to message; send into socket
client_socket.sendto(message.encode(), (server_name, server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()



