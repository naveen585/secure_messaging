import socket
from pyascon.ascon import ascon_encrypt, ascon_decrypt
import base64

key_a_to_b = bytes.fromhex("00aabbccddeeff112233445566778899")
nonce = bytes.fromhex("00000000000000000000000000000000")
key_b_to_a = bytes.fromhex("1122334455aabbccddeeff6677889900")
associated_data = b"CS645/745 Modern Cryptography: Secure Messaging"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1" # localhost
# server_host = "192.168.46.51" # different systems with same network
server_port = 6789
client_socket.connect((server_host, server_port))
while True:
    ciphertext_encoded = client_socket.recv(1024)
    if not ciphertext_encoded:
        break
    ciphertext_a_to_b = base64.b64decode(ciphertext_encoded)
    decrypted_text_a_to_b = ascon_decrypt(key_a_to_b, nonce, associated_data, ciphertext_a_to_b, variant="Ascon-128")
    if decrypted_text_a_to_b.decode().lower() == 'exit':
        print("Connection closed by the User A (server).")
        break
    print(f"Message received from User A to User B : {decrypted_text_a_to_b.decode()}")
    user_b_message = input("User B send your message to User A (type 'exit' to end): ")
    if user_b_message.lower() == 'exit':
        print("Connection closed.")
        break
    ciphertext_b_to_a = ascon_encrypt(key_b_to_a, nonce, associated_data, user_b_message.encode(), variant="Ascon-128")
    client_socket.sendall(base64.b64encode(ciphertext_b_to_a))
    
client_socket.close()
