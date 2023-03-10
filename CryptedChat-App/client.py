import socket
import keyboard
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.1.78.202' # Replace with the IP address of the server
port = 5000

client_socket.connect((host, port))

client_name = input("Enter your name: ")


while True:
    message = input(client_name + ": ")
    client_socket.send(message.encode('utf-8'))

    if message == 'exit':
        break

    reply = client_socket.recv(1024).decode('utf-8')
    print('Received reply:', reply)
    

client_socket.close()