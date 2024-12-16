import os
import json
from Crypto.PublicKey import RSA

class KeyManagement:
    def __init__(self, key_file='keys.json'):
        self.key_file = key_file
        self.keys = {}

    def generate_keys(self):
        """Generate RSA keys and store them."""
        key = RSA.generate(2048)
        self.keys['private_key'] = key.export_key().decode('utf-8')
        self.keys['public_key'] = key.publickey().export_key().decode('utf-8')
        self.save_keys()

    def save_keys(self):
        """Save keys to a JSON file."""
        with open(self.key_file, 'w') as f:
            json.dump(self.keys, f)

    def load_keys(self):
        """Load keys from a JSON file."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'r') as f:
                self.keys = json.load(f)
        else:
            print("Key file not found. Please generate keys first.")

    def get_public_key(self):
        """Return the public key."""
        return self.keys.get('public_key')

    def get_private_key(self):
        """Return the private key."""
        return self.keys.get('private_key')

if __name__ == "__main__":
    key_manager = KeyManagement()
    key_manager.generate_keys()
    key_manager.load_keys()
    print("Public Key:", key_manager.get_public_key())
    print("Private Key:", key_manager.get_private_key())
