import unittest
import logging
from logging.log_handler import CustomLogHandler

class TestCustomLogHandler(unittest.TestCase):
    
    def setUp(self):
        self.log_file = 'test.log'
        self.handler = CustomLogHandler(self.log_file)
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def test_logging(self):
        self.logger.info("Test log entry.")
        with open(self.log_file, 'r') as f:
            logs = f.readlines()
        self.assertIn("Test log entry.", logs[-1])

if __name__ == '__main__':
    unittest.main()
