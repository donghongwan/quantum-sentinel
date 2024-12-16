class NetworkConfig:
    """Network settings for AI model."""
    HOST = "localhost"
    PORT = 5000
    TIMEOUT = 30  # seconds

    @staticmethod
    def init_app(app):
        """Initialize the app with network configurations."""
        app.config['HOST'] = NetworkConfig.HOST
        app.config['PORT'] = NetworkConfig.PORT
        app.config['TIMEOUT'] = NetworkConfig.TIMEOUT

if __name__ == "__main__":
    # Example usage
    print("Network Host:", NetworkConfig.HOST)
    print("Network Port:", NetworkConfig.PORT)
