from pyascon.ascon import ascon_encrypt

key = bytes.fromhex("00112233445566778899aabbccddeeff")
nonce = bytes.fromhex("00000000000000000000000000000000")
associated_data = b"CS645/745 Modern Cryptography: Secure Messaging"
input_file = "./message_file.txt"
output_file = "./ciphertext_file.txt"
with open(input_file, 'rb') as file:
    plaintext = file.read()
ciphertext= ascon_encrypt(key, nonce, associated_data, plaintext,variant="Ascon-128")
with open(output_file, 'wb') as file:
    file.write(ciphertext)
print("File encrypted successfully.")
