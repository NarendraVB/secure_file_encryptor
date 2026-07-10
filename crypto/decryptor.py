from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

from crypto.key_manager import load_key
from utils.validator import validate_file_exists,validate_encrypted_file
from utils.file_handler import read_file, write_file,get_output_path


def decrypt_file(file_path):
        """
        Decrypt a Fernet-encrypted file.
        """

        key = load_key()
        cipher = Fernet(key)
        validate_file_exists(file_path)
        validate_encrypted_file(file_path)
        file_path = Path(file_path)

        encrypted_data = read_file(file_path)
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
        except InvalidToken:
            raise ValueError(
                "Invalid encryption key or corrupted file. Decryption failed.")

        output_dir = Path("decrypted")
        output_dir.mkdir(exist_ok=True)

        output_file = get_output_path(file_path, "decrypted")

        write_file(output_file, decrypted_data)

        return output_file
