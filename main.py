from crypto.encryptor import encrypt_file
from crypto.decryptor import decrypt_file

encrypted_file = encrypt_file("sample.txt")

print("Encrypted:", encrypted_file)

decrypted_file = decrypt_file(encrypted_file)

print("Decrypted:", decrypted_file)