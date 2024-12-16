import logging

def setup_logging(log_file='api_requests.log'):
    """Set up logging for API requests."""
    logging.basicConfig(filename=log_file, level=logging.INFO)

def log_request(request):
    """Log details of an API request."""
    logging.info(f"Request: {request.method} {request.path} - Body: {request.get_json()}")

if __name__ == "__main__":
    # Example usage
    setup_logging()
    log_request({"method": "GET", "path": "/example", "body": None})  # Simulate a request
