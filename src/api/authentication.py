from flask import request, jsonify
from functools import wraps

# Dummy user data for demonstration
users = {
    "user1": "password1",
    "user2": "password2"
}

def authenticate(username, password):
    """Authenticate a user with username and password."""
    return users.get(username) == password

def requires_auth(f):
    """Decorator to enforce authentication on API routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    print(authenticate("user1", "password1"))  # Should return True
