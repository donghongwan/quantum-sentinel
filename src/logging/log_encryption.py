from cryptography.fernet import Fernet

class LogEncryption:
    """Encryption of log files for security."""
    
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_log(self, log_data):
        """Encrypt log data."""
        return self.fernet.encrypt(log_data.encode()).decode()

    def decrypt_log(self, encrypted_data):
        """Decrypt log data."""
        return self.fernet.decrypt(encrypted_data.encode()).decode()

if __name__ == "__main__":
    # Example usage
    key = Fernet.generate_key()  # Generate a new key
    log_encryption = LogEncryption(key)

    original_log = "This is a sensitive log entry."
    encrypted_log = log_encryption.encrypt_log(original_log)
    decrypted_log = log_encryption.decrypt_log(encrypted_log)

    print("Original Log:", original_log)
    print("Encrypted Log:", encrypted_log)
    print("Decrypted Log:", decrypted_log)
