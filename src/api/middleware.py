from flask import request

def request_logging():
    """Middleware to log incoming requests."""
    print(f"Request: {request.method} {request.path} - Body: {request.get_json()}")
