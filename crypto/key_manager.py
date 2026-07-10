from cryptography.fernet import Fernet
from pathlib import Path

KEY_DIR = Path("keys")
KEY_FILE = KEY_DIR / "secret.key"


def generate_key():
    """
    Generate a new Fernet key only if one doesn't already exist.
    """
    KEY_DIR.mkdir(exist_ok=True)

    if KEY_FILE.exists():
        raise FileExistsError(
            "Encryption key already exists. Refusing to overwrite it."
        )

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


def load_key():
    """
    Load the existing encryption key.
    """
    if not KEY_FILE.exists():
        raise FileNotFoundError(
            "Encryption key not found. Generate one first."
        )

    with open(KEY_FILE, "rb") as file:
        return file.read()