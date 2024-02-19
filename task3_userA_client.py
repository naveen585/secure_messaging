import socket
from pyascon.ascon import ascon_encrypt
import base64

key_a_b = bytes.fromhex("00112233445566778899aabbccddeeff")
nonce_a_b = bytes.fromhex("00000000000000000000000000000000")
associated_data_a_b = b"CS645/745 Modern Cryptography: Secure Messaging"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1"  # Server's IP address
server_port = 6789
client_socket.connect((server_host, server_port))
while True:
    userA_message = input("User A send your message (type 'exit' to end): ")
    ciphertext = ascon_encrypt(key_a_b, nonce_a_b, associated_data_a_b, userA_message.encode(), variant="Ascon-128")
    client_socket.sendall(base64.b64encode(ciphertext))
    if userA_message.lower() == 'exit':
        break
client_socket.close()
