class ThreatModelingConfig:
    """Configuration for threat modeling."""
    THREAT_LEVELS = {
        "low": "Minimal impact and likelihood.",
        "medium": "Moderate impact and likelihood.",
        "high": "Significant impact and likelihood.",
        "critical": "Severe impact and likelihood."
    }
    DEFAULT_THREAT_LEVEL = "medium"

    @staticmethod
    def init_app(app):
        """Initialize the app with threat modeling configurations."""
        app.config['THREAT_LEVELS'] = ThreatModelingConfig.THREAT_LEVELS
        app.config['DEFAULT_THREAT_LEVEL'] = ThreatModelingConfig.DEFAULT_THREAT_LEVEL

if __name__ == "__main__":
    # Example usage
    print("Threat Levels:", ThreatModelingConfig.THREAT_LEVELS)
    print("Default Threat Level:", ThreatModelingConfig.DEFAULT_THREAT_LEVEL)
