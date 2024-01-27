# ######################################################
# Note:
# TCP socket is identified by a four-tuple value
# No need to attach server name, port
# It is acceptable to create two TCP connections on the same server/port
# doublet from the same client with different port numbers.
# ######################################################

import socket

# call DNS resolver by gethostbyname() method
server_name = socket.gethostbyname(socket.gethostname())
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sends a connection establishment request (destination port number 12000 and
# a special connection-establishment bit set in the TCP header + source port number
# that was chosen by the client)
client_socket.connect((server_name, server_port))
sentence = input('Input lowercase sentence: ')
client_socket.send(sentence.encode())
modified_sentence = client_socket.recv(1024)
print('From Server: ', modified_sentence.decode())
client_socket.close()