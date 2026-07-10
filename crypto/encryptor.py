from cryptography.fernet import Fernet
from pathlib import Path

from crypto.key_manager import load_key
from utils.validator import validate_file_exists
from utils.file_handler import read_file, write_file,get_output_path


def encrypt_file(file_path):
    """
    Encrypt a file using the stored Fernet key.
    """

    key = load_key()
    cipher = Fernet(key)
    validate_file_exists(file_path)
    file_path = Path(file_path)

    data = read_file(file_path)
    
    try:
        encrypted_data = cipher.encrypt(data)
    except Exception as e:
        print(f"Error occurred while encrypting the file: {e}")
        return None

    output_file = get_output_path(file_path, "encrypted", suffix=".enc")
    write_file(output_file, encrypted_data)

    return output_file