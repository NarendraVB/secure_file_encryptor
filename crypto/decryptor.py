from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

from crypto.key_manager import load_key
from utils.validator import (
    validate_file_exists,
    validate_encrypted_file,
)


def decrypt_file(file_path):
        """
        Decrypt a Fernet-encrypted file.
        """

        key = load_key()
        cipher = Fernet(key)
        validate_file_exists(file_path)
        validate_encrypted_file(file_path)
        file_path = Path(file_path)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
        except InvalidToken:
            print("Invalid encryption key or corrupted file. Decryption failed.")
            
        output_dir = Path("decrypted")
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / file_path.stem

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        return output_file
