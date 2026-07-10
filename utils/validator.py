from pathlib import Path


def validate_file_exists(file_path):
    """
    Ensure the supplied path exists and is a file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    if not path.is_file():
        raise ValueError(f"'{file_path}' is not a file.")


def validate_encrypted_file(file_path):
    """
    Ensure the file has the expected .enc extension.
    """
    path = Path(file_path)

    if path.suffix != ".enc":
        raise ValueError("Expected a .enc encrypted file.")