from flask import request, jsonify
from time import time

class Throttle:
    def __init__(self, limit, period):
        self.limit = limit
        self.period = period
        self.requests = {}

    def is_allowed(self, key):
        """Check if a request is allowed based on throttling rules."""
        current_time = time()
        if key not in self.requests:
            self.requests[key] = []

        # Remove outdated requests
        self.requests[key] = [timestamp for timestamp in self.requests[key] if current_time - timestamp < self.period]

        if len(self.requests[key]) < self.limit:
            self.requests[key].append(current_time)
            return True
        return False

throttle = Throttle(limit=10, period=60)  # 10 requests per minute

def throttle_requests(f):
    """Decorator to enforce throttling on API routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.remote_addr  # Use IP address as the key
        if not throttle.is_allowed(key):
            return jsonify({"message": "Too many requests"}), 429
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    print("Throttle module loaded.")
