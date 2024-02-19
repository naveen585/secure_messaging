from pyascon.ascon import ascon_decrypt

key = bytes.fromhex("00112233445566778899aabbccddeeff")
nonce = bytes.fromhex("00000000000000000000000000000000")
associated_data = b"CS645/745 Modern Cryptography: Secure Messaging"
input_file = "./ciphertext_file.txt"
with open(input_file, 'rb') as file:
    ciphertext = file.read()
decrypted_text = ascon_decrypt(key, nonce, associated_data, ciphertext,variant="Ascon-128")
print(f"The encrypted text which received is : {decrypted_text.decode()}")
