import os
import secrets

class SecureRandom:
    @staticmethod
    def generate_random_bytes(n):
        """Generate secure random bytes."""
        return os.urandom(n)

    @staticmethod
    def generate_secure_random_int(min_value, max_value):
        """Generate a secure random integer within a specified range."""
        return secrets.randbelow(max_value - min_value + 1) + min_value

if __name__ == "__main__":
    random_bytes = SecureRandom.generate_random_bytes(16)
    print("Secure Random Bytes:", random_bytes.hex())
    random_int = SecureRandom.generate_secure_random_int(1, 100)
    print("Secure Random Integer:", random_int)
