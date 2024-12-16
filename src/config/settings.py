import os

class Config:
    """Main configuration settings."""
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

    @staticmethod
    def init_app(app):
        """Initialize the app with the configuration."""
        app.config.from_object(Config)

if __name__ == "__main__":
    # Example usage
    print("Debug:", Config.DEBUG)
    print("Database URI:", Config.DATABASE_URI)
