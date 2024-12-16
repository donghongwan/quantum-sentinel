from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

class DigitalSignatures:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def sign(self, message):
        """Sign a message using RSA."""
        rsa_private_key = RSA.import_key(self.private_key)
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(rsa_private_key).sign(message_hash)
        return base64.b64encode(signature).decode('utf-8')

    def verify(self, message, signature):
        """Verify a signed message using RSA."""
        rsa_public_key = RSA.import_key(self.public_key)
        message_hash = SHA256.new(message.encode())
        try:
            pkcs1_15.new(rsa_public_key).verify(message_hash, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False

if __name__ == "__main__":
    ds = DigitalSignatures()
    message = "This is a test message for digital signing."
    signature = ds.sign(message)
    print("Signature:", signature)
    is_valid = ds.verify(message, signature)
    print("Is the signature valid?", is_valid)
