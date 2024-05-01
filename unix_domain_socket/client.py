import socket
import os
import sys

client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = os.path.expanduser('~/socket_file')
print(f'connecting to {server_address}')

# Connect to the server socket
try:
    client_socket.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = b'Sending a message to the server side'
    client_socket.sendall(message)
    # Set timeout to 2 seconds, so that if there is no response from the server, the program will move on.
    client_socket.settimeout(2)

    try:
        while True:
            data = client_socket.recv(32).decode('utf-8')
            if data:
                print('Server response: ' + data)
            else:
                break
    except socket.timeout:
        print('Socket timeout, ending listening for server messages')

finally:
    print('Closing current connection')
    client_socket.close()