class DataPrivacyConfig:
    """Data privacy settings."""
    DATA_ENCRYPTION_ENABLED = True
    DATA_RETENTION_POLICY = "Data will be retained for 2 years."
    USER_DATA_ACCESS_LOGGING = True

    @staticmethod
    def init_app(app):
        """Initialize the app with data privacy configurations."""
        app.config['DATA_ENCRYPTION_ENABLED'] = DataPrivacyConfig.DATA_ENCRYPTION_ENABLED
        app.config['DATA_RETENTION_POLICY'] = DataPrivacyConfig.DATA_RETENTION_POLICY
        app.config['USER_DATA_ACCESS_LOGGING'] = DataPrivacyConfig.USER_DATA_ACCESS_LOGGING

if __name__ == "__main__":
    # Example usage
    print("Data Encryption Enabled:", DataPrivacyConfig.DATA_ENCRYPTION_ENABLED)
    print("Data Retention Policy:", DataPrivacyConfig.DATA_RETENTION_POLICY)
