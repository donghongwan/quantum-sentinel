class ComplianceConfig:
    """Compliance-related configurations."""
    GDPR_COMPLIANT = True
    CCPA_COMPLIANT = True
    DATA_RETENTION_PERIOD = 365  # days

    @staticmethod
    def init_app(app):
        """Initialize the app with compliance configurations."""
        app.config['GDPR_COMPLIANT'] = ComplianceConfig.GDPR_COMPLIANT
        app.config['CCPA_COMPLIANT'] = ComplianceConfig.CCPA_COMPLIANT
        app.config['DATA_RETENTION_PERIOD'] = ComplianceConfig.DATA_RETENTION_PERIOD

if __name__ == "__main__":
    # Example usage
    print("GDPR Compliant:", ComplianceConfig.GDPR_COMPLIANT)
    print("Data Retention Period:", ComplianceConfig.DATA_RETENTION_PERIOD)
