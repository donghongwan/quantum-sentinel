import time
import unittest

class TestPerformance(unittest.TestCase):
    
    def test_performance(self):
        start_time = time.time()
        # Call the function you want to test
        time.sleep(1)  # Simulate a function call
        end_time = time.time()
        self.assertLess(end_time - start_time, 2)  # Ensure it runs within 2 seconds

if __name__ == '__main__':
    unittest.main()
