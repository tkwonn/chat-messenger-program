####################################################################################################
# Run this program and wait for the response from gaia.cs.umass.edu
####################################################################################################

from socket import *

server_name = 'gaia.cs.umass.edu'
server_port = 80

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

# client_socket.send(b'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n')
# response = client_socket.recv(2048)

# For more larger file
request = b'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n'
client_socket.send(request)

response = b''

while True:
    data = client_socket.recv(4096)
    if not data:
        break
    response += data

# By default, decode() method uses 'utf-8' encoding, but we're explicitly specifying it here
print("Server Response: ", response.decode('utf-8'))

client_socket.close()
