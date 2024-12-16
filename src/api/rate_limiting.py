from flask import request, jsonify
from time import time

class RateLimiter:
    def __init__(self, limit, period):
        self.limit = limit
        self.period = period
        self.requests = {}

    def is_allowed(self, key):
        """Check if a request is allowed based on rate limiting."""
        current_time = time()
        if key not in self.requests:
            self.requests[key] = []

        # Remove outdated requests
        self.requests[key] = [timestamp for timestamp in self.requests[key] if current_time - timestamp < self.period]

        if len(self.requests[key]) < self.limit:
            self.requests[key].append(current_time)
            return True
        return False

rate_limiter = RateLimiter(limit=5, period=60)  # 5 requests per minute

def limit_requests(f):
    """Decorator to enforce rate limiting on API routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.remote_addr  # Use IP address as the key
        if not rate_limiter.is_allowed(key):
            return jsonify({"message": "Too many requests"}), 429
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    limiter = RateLimiter(limit=5, period=60)
    print(limiter.is_allowed("192.168.1.1"))  # Should return True or False based on the request count
