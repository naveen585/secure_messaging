import socket
from pyascon.ascon import ascon_decrypt, ascon_encrypt
import base64

key_a_to_b = bytes.fromhex("00aabbccddeeff112233445566778899")
nonce = bytes.fromhex("00000000000000000000000000000000")
key_b_to_a = bytes.fromhex("1122334455aabbccddeeff6677889900")
associated_data = b"CS645/745 Modern Cryptography: Secure Messaging"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1" # localhost
# server_host = "0.0.0.0" # same network with different systems
server_port = 6789
server_socket.bind((server_host, server_port))
server_socket.listen(3)
client_conn, client_addr = server_socket.accept()
print("Connection has been established.")
while True:
    user_a_message = input("User A send your message to User B (type 'exit' to end): ")
    if user_a_message.lower() == 'exit':
        print("Connection closed.")
        break
    ciphertext_a_to_b = ascon_encrypt(key_a_to_b, nonce, associated_data, user_a_message.encode(), variant="Ascon-128")
    client_conn.sendall(base64.b64encode(ciphertext_a_to_b))
    encoded_ciphertext = client_conn.recv(1024)
    if not encoded_ciphertext:
        break
    ciphertext = base64.b64decode(encoded_ciphertext)
    decrypted_text_b_to_a = ascon_decrypt(key_b_to_a, nonce, associated_data, ciphertext, variant="Ascon-128")
    if decrypted_text_b_to_a.decode().lower() == 'exit':
        print("Connection closed")
        break
    print(f"Message received from User B to User A : {decrypted_text_b_to_a.decode()}")
server_socket.close()
