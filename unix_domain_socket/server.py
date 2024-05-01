import socket
import os

# AF_UNIX socket domain is used for communication between processes on the same host.
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# This will create the socket file in the user's home directory where your user has write permissions.
server_address = os.path.expanduser('~/socket_file')

# Make sure the socket file does not already exist
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'Starting up on {server_address}')

server_socket.bind(server_address)

# Listen to at most 1 connection at a time.
server_socket.listen(1)

while True:
    # accept connections from outside
    # The address returned by accept() is an empty string when conncting to a UNIX domain socket.
    (client_socket, client_address) = server_socket.accept()
    print(f'Client socket: {client_socket}')
    print(f'Client address: {client_address}') # empty string

    try:
        print('connection from the client')

        while True:
            # Receives the data in 16 byte chunks from the client
            data = client_socket.recv(16).decode('utf-8')
            print('Received: ' + data)

            if data:
                client_socket.sendall(data.upper().encode())
            else:
                print('no data from the client')
                break

    # Clean up the connection
    finally:
        print("Closing current connection")
        client_socket.close()