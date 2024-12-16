from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

class SymmetricEncryption:
    def __init__(self):
        self.key = self.generate_key()

    @staticmethod
    def generate_key():
        """Generate a random AES key."""
        return os.urandom(16)  # AES-128

    def encrypt(self, plain_text):
        """Encrypt the plain text using AES encryption."""
        cipher = AES```python
.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def decrypt(self, iv, ct):
        """Decrypt the cipher text using AES decryption."""
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return plain_text

if __name__ == "__main__":
    symmetric_encryption = SymmetricEncryption()
    iv, ct = symmetric_encryption.encrypt("Advanced Quantum Sentinel Security!")
    print("IV:", iv)
    print("Cipher Text:", ct)
    decrypted_text = symmetric_encryption.decrypt(iv, ct)
    print("Decrypted Text:", decrypted_text)
