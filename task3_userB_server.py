import socket
from pyascon.ascon import ascon_decrypt
import base64

key_a_b = bytes.fromhex("00112233445566778899aabbccddeeff")
nonce_a_b = bytes.fromhex("00000000000000000000000000000000")
associated_data_a_b = b"CS645/745 Modern Cryptography: Secure Messaging"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1"
server_port = 6789
server_socket.bind((server_host, server_port))
server_socket.listen(3)
client_conn, client_addr = server_socket.accept()
print("Connection has been established.")
while True:
    ciphertext_encoded = client_conn.recv(1024)
    ciphertext = base64.b64decode(ciphertext_encoded)
    decrypted_text = ascon_decrypt(key_a_b, nonce_a_b, associated_data_a_b, ciphertext, variant="Ascon-128")
    if decrypted_text.decode().lower() == 'exit':
        break
    print(f"The message received from User A to B is: {decrypted_text.decode()}")
server_socket.close()
