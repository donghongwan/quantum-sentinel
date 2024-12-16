class FeatureFlags:
    """Feature flags for experimental features."""
    ENABLE_NEW_FEATURE_X = False
    ENABLE_NEW_FEATURE_Y = True
    ENABLE_BETA_TESTING = False

    @staticmethod
    def init_app(app):
        """Initialize the app with feature flags."""
        app.config['ENABLE_NEW_FEATURE_X'] = FeatureFlags.ENABLE_NEW_FEATURE_X
        app.config['ENABLE_NEW_FEATURE_Y'] = FeatureFlags.ENABLE_NEW_FEATURE_Y
        app.config['ENABLE_BETA_TESTING'] = FeatureFlags.ENABLE_BETA_TESTING

if __name__ == "__main__":
    # Example usage
    print("Feature X Enabled:", FeatureFlags.ENABLE_NEW_FEATURE_X)
    print("Feature Y Enabled:", FeatureFlags.ENABLE_NEW_FEATURE_Y)
