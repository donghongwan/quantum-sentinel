from flask import request, jsonify

def get_api_version():
    """Get the API version from the request headers."""
    return request.headers.get('API-Version', '1.0')

def versioned_route(version):
    """Decorator to handle versioned routes."""
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            api_version = get_api_version()
            if api_version != version:
                return jsonify({"message": f"API version {version} required"}), 400
            return f(*args, **kwargs)
        return decorated
    return decorator

if __name__ == "__main__":
    # Example usage
    print(get_api_version())  # Simulate getting the API version from headers
