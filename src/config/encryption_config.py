from cryptography.fernet import Fernet

class EncryptionConfig:
    """Encryption settings."""
    SECRET_KEY = Fernet.generate_key()  # Generate a new key
    fernet = Fernet(SECRET_KEY)

    @staticmethod
    def encrypt(data):
        """Encrypt data using the secret key."""
        return EncryptionConfig.fernet.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(token):
        """Decrypt data using the secret key."""
        return EncryptionConfig.fernet.decrypt(token.encode()).decode()

if __name__ == "__main__":
    # Example usage
    original_data = "Hello, World!"
    encrypted_data = EncryptionConfig.encrypt(original_data)
    decrypted_data = EncryptionConfig.decrypt(encrypted_data)

    print("Original Data:", original_data)
    print("Encrypted Data:", encrypted_data)
    print("Decrypted Data:", decrypted_data)
