from flask import request, jsonify
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

def cache_response(timeout=60):
    """Decorator to cache API responses."""
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            cache_key = request.path
            cached_response = cache.get(cache_key)
            if cached_response is not None:
                return cached_response
            response = f(*args, **kwargs)
            cache.set(cache_key, response, timeout)
            return response
        return decorated
    return decorator

if __name__ == "__main__":
    # Example usage
    print("Caching module loaded.")
