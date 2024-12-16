class APIConfig:
    """API-specific configurations."""
    API_VERSION = '1.0'
    RATE_LIMIT = '100 per hour'
    ALLOWED_ORIGINS = ['http://localhost:3000']

    @staticmethod
    def init_app(app):
        """Initialize the app with API-specific configurations."""
        app.config['API_VERSION'] = APIConfig.API_VERSION
        app.config['RATE_LIMIT'] = APIConfig.RATE_LIMIT
        app.config['ALLOWED_ORIGINS'] = APIConfig.ALLOWED_ORIGINS

if __name__ == "__main__":
    # Example usage
    print("API Version:", APIConfig.API_VERSION)
    print("Rate Limit:", APIConfig.RATE_LIMIT)
