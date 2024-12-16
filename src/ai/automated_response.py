class AutomatedResponse:
    def __init__(self):
        self.responses = {
            "high": "Immediate action required: escalate to the security team.",
            "medium": "Monitor the situation closely and prepare a report.",
            "low": "No immediate action required, but keep an eye on the logs."
        }

    def generate_response(self, threat_level):
        """Generate an automated response based on the threat level."""
        return self.responses.get(threat_level, "Unknown threat level.")

if __name__ == "__main__":
    # Example usage
    ar = AutomatedResponse()
    threat_level = "high"
    response = ar.generate_response(threat_level)
    print("Automated Response:", response)
