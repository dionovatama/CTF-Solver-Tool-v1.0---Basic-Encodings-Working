# CTF Solver Tool

Automated encoding detection dan cryptography decryption tool untuk CTF challenges.

## Status
✅ **Working!**

## Features Implemented

- [x] Base64 detection & decoding
- [x] Hexadecimal detection & decoding
- [x] ROT13 decoding
- [x] Atbash cipher
- [x] Caesar cipher (brute force all 26 shifts)
- [x] Auto-detect encoding
- [x] CLI interface dengan colored output

## Installation

```bash
# Clone
git clone https://github.com/dionovatama/CTF-Solver-Tool-v1.0---Basic-Encodings-Working.git
cd ctf-solver

# Setup
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install
pip install -r requirements.txt
```

## Usage

```bash
# Auto-detect
python main.py auto "SGVsbG8gV29ybGQ="

# Specific decoders
python main.py base64 "SGVsbG8gV29ybGQ="
python main.py hex "48656c6c6f"
python main.py rot13 "Uryyb"
python main.py caesar "IFMMP"
```

## Output Example
