from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

class CryptographicProtocols:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def sign_message(self, message):
        """Sign a message using RSA digital signature."""
        rsa_private_key = RSA.import_key(self.private_key)
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(rsa_private_key).sign(message_hash)
        return base64.b64encode(signature).decode('utf-8')

    def verify_signature(self, message, signature):
        """Verify a signed message using RSA digital signature."""
        rsa_public_key = RSA.import_key(self.public_key)
        message_hash = SHA256.new(message.encode())
        try:
            pkcs1_15.new(rsa_public_key).verify(message_hash, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False

if __name__ == "__main__":
    protocol = CryptographicProtocols()
    message = "Hello, Quantum Sentinel with Digital Signatures!"
    signature = protocol.sign_message(message)
    print("Signature:", signature)
    is_valid = protocol.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)
