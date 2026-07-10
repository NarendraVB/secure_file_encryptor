import sys

from crypto.encryptor import encrypt_file
from crypto.decryptor import decrypt_file
from crypto.key_manager import generate_key


def print_usage():
    print("\nSecure File Encryption Utility")
    print("-------------------------------")
    print("Usage:")
    print("  python main.py generate-key")
    print("  python main.py encrypt <file>")
    print("  python main.py decrypt <encrypted_file>")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    try:
        if command == "generate-key":
            generate_key()
            print("Encryption key generated successfully.")

        elif command == "encrypt":
            if len(sys.argv) != 3:
                print("Usage: python main.py encrypt <file>")
                return

            output = encrypt_file(sys.argv[2])
            print(f"Encrypted file saved to: {output}")

        elif command == "decrypt":
            if len(sys.argv) != 3:
                print("Usage: python main.py decrypt <encrypted_file>")
                return

            output = decrypt_file(sys.argv[2])
            print(f"Decrypted file saved to: {output}")

        else:
            print(f"Unknown command: {command}")
            print_usage()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()