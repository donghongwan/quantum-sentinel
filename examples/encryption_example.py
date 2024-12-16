from log_management.log_encryption import LogEncryption
from cryptography.fernet import Fernet

def encryption_example():
    key = Fernet.generate_key()
    log_encryption = LogEncryption(key)

    original_log = "Sensitive log entry."
    encrypted_log = log_encryption.encrypt_log(original_log)
    decrypted_log = log_encryption.decrypt_log(encrypted_log)

    print("Original Log:", original_log)
    print("Encrypted Log:", encrypted_log)
    print("Decrypted Log:", decrypted_log)

if __name__ == "__main__":
    encryption_example()
