from flask import request
import logging

class ApiMonitoring:
    def __init__(self):
        self.request_count = 0

    def log_request(self):
        """Log API request details."""
        self.request_count += 1
        logging.info(f"Request {self.request_count}: {request.method} {request.path}")

    def get_request_count(self):
        """Get the total number of requests received."""
        return self.request_count

api_monitoring = ApiMonitoring()

def monitor_requests(f):
    """Decorator to monitor API requests."""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_monitoring.log_request()
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    api_monitoring.log_request()
    print(api_monitoring.get_request_count())  # Should return the count of requests
