from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

class SecureMessaging:
    def __init__(self):
        self.key = os.urandom(16)  # AES-128

    def encrypt_message(self, message):
        """Encrypt a message using AES."""
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def decrypt_message(self, iv, ct):
        """Decrypt a message using AES."""
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return plain_text

if __name__ == "__main__":
    messaging = SecureMessaging()
    iv, ct = messaging.encrypt_message("Hello, secure messaging!")
    print("IV:", iv)
    print("Cipher Text:", ct)
    decrypted_text = messaging.decrypt_message(iv, ct)
    print("Decrypted Text:", decrypted_text)
