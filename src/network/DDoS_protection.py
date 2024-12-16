import time
from collections import defaultdict

class DDoSProtection:
    def __init__(self, threshold=100):
        self.threshold = threshold
        self.requests = defaultdict(list)

    def log_request(self, ip):
        """Log a request from an IP address."""
        current_time = time.time()
        self.requests[ip].append(current_time)
        self.cleanup_requests(ip)

    def cleanup_requests(self, ip):
        """Remove requests older than 1 minute."""
        current_time = time.time()
        self.requests[ip] = [req for req in self.requests[ip] if current_time - req < 60]

    def is_under_attack(self, ip):
        """Check if the IP is making too many requests."""
        if len(self.requests[ip]) > self.threshold:
            print(f"Potential DDoS attack detected from {ip}!")
            return True
        return False

if __name__ == "__main__":
    # Example usage
    ddos_protection = DDoSProtection()

    # Simulate logging requests
    for _ in range(105):  # Simulating 105 requests from the same IP
        ddos_protection.log_request("192.168.1.1")
        if ddos_protection.is_under_attack("192.168.1.1"):
            break
