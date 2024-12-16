class PerformanceConfig:
    """Performance tuning settings."""
    MAX_CONCURRENT_REQUESTS = 100
    TIMEOUT_LIMIT = 60  # seconds
    CACHE_SIZE = 256  # MB

    @staticmethod
    def init_app(app):
        """Initialize the app with performance configurations."""
        app.config['MAX_CONCURRENT_REQUESTS'] = PerformanceConfig.MAX_CONCURRENT_REQUESTS
        app.config['TIMEOUT_LIMIT'] = PerformanceConfig.TIMEOUT_LIMIT
        app.config['CACHE_SIZE'] = PerformanceConfig.CACHE_SIZE

if __name__ == "__main__":
    # Example usage
    print("Max Concurrent Requests:", PerformanceConfig.MAX_CONCURRENT_REQUESTS)
    print("Cache Size:", PerformanceConfig.CACHE_SIZE)
