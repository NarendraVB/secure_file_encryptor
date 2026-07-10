from cryptography.fernet import Fernet
from pathlib import Path

KEY_DIR = Path("keys")
KEY_FILE = KEY_DIR / "secret.key"


def generate_key():
    """
    Generate and save a new Fernet key.
    """
    KEY_DIR.mkdir(exist_ok=True)

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


def load_key():
    """
    Load the existing encryption key.
    """
    with open(KEY_FILE, "rb") as file:
        return file.read()