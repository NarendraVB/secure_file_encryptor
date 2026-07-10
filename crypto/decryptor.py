from pathlib import Path

from cryptography.fernet import Fernet

from crypto.key_manager import load_key


def decrypt_file(file_path):
    """
    Decrypt a Fernet-encrypted file.
    """

    key = load_key()
    cipher = Fernet(key)

    file_path = Path(file_path)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    output_dir = Path("decrypted")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / file_path.stem

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    return output_file