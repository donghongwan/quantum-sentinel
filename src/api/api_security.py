from flask import request, jsonify
from functools import wraps

def api_key_required(f):
    """Decorator to enforce API key authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != 'your_api_key_here':  # Replace with your actual API key check
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    print("API security module loaded.")
