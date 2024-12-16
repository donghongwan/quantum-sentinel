from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class AsymmetricEncryption:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def encrypt(self, plain_text):
        """Encrypt the plain text using RSA public key."""
        rsa_public_key = RSA.import_key(self.public_key)
        cipher = PKCS1_OAEP.new(rsa_public_key)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return base64.b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        """Decrypt the cipher text using RSA private key."""
        rsa_private_key = RSA.import_key(self.private_key)
        cipher = PKCS1_OAEP.new(rsa_private_key)
        decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text))
        return decrypted_text.decode('utf-8')

if __name__ == "__main__":
    asymmetric_encryption = AsymmetricEncryption()
    encrypted_text = asymmetric_encryption.encrypt("Hello, Quantum Sentinel with Asymmetric Encryption!")
    print("Encrypted Text:", encrypted_text)
    decrypted_text = asymmetric_encryption.decrypt(encrypted_text)
    print("Decrypted Text:", decrypted_text)
