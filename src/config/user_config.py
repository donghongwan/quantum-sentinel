class UserConfig:
    """User settings and preferences."""
    DEFAULT_LANGUAGE = "en"
    DEFAULT_TIMEZONE = "UTC"
    MAX_LOGIN_ATTEMPTS = 5

    @staticmethod
    def init_app(app):
        """Initialize the app with user configurations."""
        app.config['DEFAULT_LANGUAGE'] = UserConfig.DEFAULT_LANGUAGE
        app.config['DEFAULT_TIMEZONE'] = UserConfig.DEFAULT_TIMEZONE
        app.config['MAX_LOGIN_ATTEMPTS'] = UserConfig.MAX_LOGIN_ATTEMPTS

if __name__ == "__main__":
    # Example usage
    print("Default Language:", UserConfig.DEFAULT_LANGUAGE)
    print("Max Login Attempts:", UserConfig.MAX_LOGIN_ATTEMPTS)
