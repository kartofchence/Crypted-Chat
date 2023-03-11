import socket
import keyboard
import sys
import genkeys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    modulus_length = 1024

    key = RSA.generate(modulus_length)#private key

    pub_key = key.publickey()#public key

    return key, pub_key


def encrypt_private_key(a_message, private_key):
    
    a_message = a_message.encode()
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    print(encrypted_msg)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(encoded_encrypted_msg)
    return encoded_encrypted_msg

def decrypt_public_key(encoded_encrypted_msg, public_key):
    
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    print(decoded_encrypted_msg)
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    print(decoded_decrypted_msg)
    #return decoded_decrypted_msg

host = '10.1.78.202' # Replace with the IP address of the server
port = 5000

client_socket.connect((host, port))

client_name = input("Enter your name: ")


while True:
    message = encrypt_private_key(input(client_name + ": "), genkeys.public)
    client_socket.send(message)

    if message == 'exit':
        break

    reply = client_socket.recv(1024).decode('utf-8')
    decoded = decrypt_public_key(reply, genkeys.private)
    print('Received reply:', decoded)
    

client_socket.close()