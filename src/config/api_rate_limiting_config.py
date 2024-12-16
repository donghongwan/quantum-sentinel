class APIRateLimitingConfig:
    """API rate limiting settings."""
    RATE_LIMIT_ENABLED = True
    MAX_REQUESTS_PER_MINUTE = 60
    MAX_REQUESTS_PER_IP = 100

    @staticmethod
    def init_app(app):
        """Initialize the app with API rate limiting configurations."""
        app.config['RATE_LIMIT_ENABLED'] = APIRateLimitingConfig.RATE_LIMIT_ENABLED
        app.config['MAX_REQUESTS_PER_MINUTE'] = APIRateLimitingConfig.MAX_REQUESTS_PER_MINUTE
        app.config['MAX_REQUESTS_PER_IP'] = APIRateLimitingConfig.MAX_REQUESTS_PER_IP

if __name__ == "__main__":
    # Example usage
    print("Rate Limit Enabled:", APIRateLimitingConfig.RATE_LIMIT_ENABLED)
    print("Max Requests Per Minute:", APIRateLimitingConfig.MAX_REQUESTS_PER_MINUTE)
