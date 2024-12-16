import unittest
from log_management.log_encryption import LogEncryption
from cryptography.fernet import Fernet

class TestLogEncryption(unittest.TestCase):
    
    def setUp(self):
        self.key = Fernet.generate_key()
        self.log_encryption = LogEncryption(self.key)

    def test_encryption_decryption(self):
        original_log = "Sensitive log entry."
        encrypted_log = self.log_encryption.encrypt_log(original_log)
        decrypted_log = self.log_encryption.decrypt_log(encrypted_log)
        self.assertEqual(original_log, decrypted_log)

    def test_invalid_decryption(self):
        with self.assertRaises(Exception):
            self.log_encryption.decrypt_log("invalid_encrypted_data")

if __name__ == '__main__':
    unittest.main()
