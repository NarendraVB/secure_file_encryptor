# 🔐 Secure File Encryption Utility

A secure command-line file encryption utility built in Python using the `cryptography` library's **Fernet** implementation. This project demonstrates modern symmetric encryption, secure key management, file integrity protection, and professional software architecture.

---

## 📖 Overview

Sensitive files stored on a computer are vulnerable if the storage device is lost, stolen, or compromised.

This project protects **data at rest** by encrypting files using **Fernet (AES-based authenticated encryption)**.

It also demonstrates secure software engineering principles including:

- Secure key generation
- Key management
- Input validation
- File integrity verification
- Modular architecture
- Automated testing
- Professional Git workflow

---

# Features

- Generate secure encryption keys
- Encrypt any file
- Decrypt encrypted files
- AES-based authenticated encryption (Fernet)
- File integrity verification
- Prevent accidental key overwrite
- Input validation
- Clean CLI interface
- Automated tests
- Modular project structure

---

# Project Structure

```
secure_file_encryptor/
│
├── crypto/
│   ├── key_manager.py
│   ├── encryptor.py
│   └── decryptor.py
│
├── utils/
│   ├── validator.py
│   └── file_handler.py
│
├── tests/
│   └── test_project.py
│
├── keys/
├── encrypted/
├── decrypted/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd secure_file_encryptor
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

## Generate Encryption Key

```bash
python main.py generate-key
```

---

## Encrypt a File

```bash
python main.py encrypt sample.txt
```

Output

```
encrypted/sample.txt.enc
```

---

## Decrypt a File

```bash
python main.py decrypt encrypted/sample.txt.enc
```

Output

```
decrypted/sample.txt
```

---

# Example Workflow

```
sample.txt

↓

Encrypt

↓

sample.txt.enc

↓

Decrypt

↓

sample.txt
```

---

# Security Features

- Fernet authenticated encryption
- AES encryption
- Secure random key generation
- Key overwrite prevention
- Input validation
- Integrity verification
- Tamper detection
- Binary file handling
- Secure error handling

---

# Threat Model

This project protects against:

- Lost laptops
- Stolen USB drives
- Unauthorized storage access
- Cloud storage leaks
- File tampering

This project does **not** protect against:

- Malware on a running system
- Stolen encryption keys
- Memory dumping
- Screen recording
- Keyloggers

---

# Technologies Used

- Python 3
- cryptography
- pathlib
- pytest

---

# Testing

Run all tests

```bash
pytest
```

Expected output

```
5 passed
```

---

# Cybersecurity Concepts Learned

- Symmetric Encryption
- Encryption vs Hashing
- AES
- Fernet
- Confidentiality
- Integrity
- Key Management
- Cryptographically Secure Random Number Generation (CSPRNG)
- Threat Modeling
- Secure File Handling
- Input Validation
- Secure Error Handling
- Fail Securely
- Separation of Concerns

---

# Future Improvements

- Password-based encryption (PBKDF2 / Argon2)
- Chunked encryption for large files
- Logging and auditing
- GUI interface
- Secure key rotation
- Cloud KMS integration
- Digital signatures
- Multi-user support

---

# License

This project is intended for educational purposes as part of the **CyberSpec Cybersecurity Roadmap**.

---