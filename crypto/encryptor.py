from cryptography.fernet import Fernet
from pathlib import Path

from crypto.key_manager import load_key


def encrypt_file(file_path):
    """
    Encrypt a file using the stored Fernet key.
    """

    key = load_key()
    cipher = Fernet(key)

    file_path = Path(file_path)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    output_file = Path("encrypted") / f"{file_path.name}.enc"

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    return output_file