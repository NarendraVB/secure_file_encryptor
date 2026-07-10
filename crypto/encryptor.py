from cryptography.fernet import Fernet
from pathlib import Path

from crypto.key_manager import load_key
from utils.validator import validate_file_exists


def encrypt_file(file_path):
    """
    Encrypt a file using the stored Fernet key.
    """

    key = load_key()
    cipher = Fernet(key)
    validate_file_exists(file_path)
    file_path = Path(file_path)

    with open(file_path, "rb") as file:
        data = file.read()
    try:
        encrypted_data = cipher.encrypt(data)
    except Exception as e:
        print(f"Error occurred while encrypting the file: {e}")
        return None

    output_file = Path("encrypted") / f"{file_path.name}.enc"

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    return output_file