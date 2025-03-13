from Crypto.Cipher import AES
import base64
import os

# Generate a 32-byte secret key (must be securely stored)

# Ensure the key is exactly 32 bytes
DEFAULT_SECRET_KEY = b'your_32_byte_secret_key_________'  # Adjust to make it 32 bytes

# Get secret key from environment variable or use default
SECRET_KEY = os.environ.get("INSTA_FILL_SECRET_KEY")

if SECRET_KEY is None:
    SECRET_KEY = DEFAULT_SECRET_KEY  # Use the corrected 32-byte default key
else:
    SECRET_KEY = SECRET_KEY.encode()  # Convert string to bytes only if needed

# Check key length and print warning if incorrect
if len(SECRET_KEY) not in [16, 24, 32]:
    raise ValueError(f"Incorrect AES key length ({len(SECRET_KEY)} bytes). Must be 16, 24, or 32 bytes.")
def pad(text):
    """Pads text to 16 bytes for AES encryption."""
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    """Removes padding from decrypted text."""
    return text[:-ord(text[-1])]

def encrypt(text):
    """Encrypts text using AES."""
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(text).encode())
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(encrypted_text):
    """Decrypts AES-encrypted text."""
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_text))
    return unpad(decrypted_bytes.decode())
