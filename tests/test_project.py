from pathlib import Path
import pytest

from crypto.key_manager import generate_key, load_key
from crypto.encryptor import encrypt_file
from crypto.decryptor import decrypt_file
from utils.validator import (
    validate_file_exists,
    validate_encrypted_file,
)


def test_key_generation_and_loading():
    """Test key generation and loading."""

    try:
        key = generate_key()
    except FileExistsError:
        key = load_key()

    assert isinstance(key, bytes)
    assert len(load_key()) > 0


def test_encrypt_and_decrypt_workflow():
    """Test complete encryption and decryption workflow."""

    sample = Path("sample.txt")
    original_data = b"CyberSpec Encryption Test"

    sample.write_bytes(original_data)

    encrypted_file = encrypt_file(sample)

    assert encrypted_file.exists()

    decrypted_file = decrypt_file(encrypted_file)

    assert decrypted_file.exists()
    assert decrypted_file.read_bytes() == original_data


def test_validate_missing_file():
    """Validator should reject missing files."""

    with pytest.raises(FileNotFoundError):
        validate_file_exists("missing.txt")


def test_validate_wrong_extension():
    """Validator should reject non-encrypted files."""

    with pytest.raises(ValueError):
        validate_encrypted_file("sample.txt")


def test_decrypt_tampered_file():
    """Tampered encrypted files should not decrypt."""

    sample = Path("tamper.txt")
    sample.write_text("CyberSpec")

    encrypted = encrypt_file(sample)

    # Corrupt the encrypted file
    data = encrypted.read_bytes()
    corrupted = data[:-1] + b"x"
    encrypted.write_bytes(corrupted)

    with pytest.raises(ValueError):
        decrypt_file(encrypted)