from pathlib import Path


def read_file(file_path):
    """
    Read a file in binary mode.
    """
    path = Path(file_path)

    with open(path, "rb") as file:
        return file.read()


def write_file(file_path, data):
    """
    Write binary data to a file.
    """
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as file:
        file.write(data)


def get_output_path(input_file, output_dir, suffix=""):
    """
    Generate an output path while preserving the original filename.

    Example:
        sample.txt -> encrypted/sample.txt.enc
        sample.txt.enc -> decrypted/sample.txt
    """
    input_path = Path(input_file)
    output_directory = Path(output_dir)

    output_directory.mkdir(exist_ok=True)

    if suffix:
        return output_directory / f"{input_path.name}{suffix}"

    return output_directory / input_path.stem