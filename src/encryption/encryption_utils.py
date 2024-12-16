import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class EncryptionUtils:
    @staticmethod
    def generate_key():
        """Generate a random AES key."""
        return os.urandom(16)  # AES-128

    @staticmethod
    def encrypt(plain_text, key):
        """Encrypt the plain text using AES encryption."""
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    @staticmethod
    def decrypt(iv, ct, key):
        """Decrypt the cipher text using AES decryption."""
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return plain_text

if __name__ == "__main__":
    key = EncryptionUtils.generate_key()
    iv, ct = EncryptionUtils.encrypt("Hello, Quantum Sentinel!", key)
    print("IV:", iv)
    print("Cipher Text:", ct)
    decrypted_text = EncryptionUtils.decrypt(iv, ct, key)
    print("Decrypted Text:", decrypted_text)
