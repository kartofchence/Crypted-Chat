import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.1.78.202' # Replace with your own IP address
port = 5000

server_socket.bind((host, port))
server_socket.listen()

print('Server is running on {}:{}'.format(host, port))
server_name = input("Enter your name: ")
client_socket, client_address = server_socket.accept()



print('Connected by', client_address,'  Adress:', client_address)

while True:
    message = client_socket.recv(1024).decode('utf-8')
    print('Received message:', message)

    if message == 'exit':
        break

    reply = input(server_name + ': ')
    client_socket.send(reply.encode('utf-8'))

client_socket.close()