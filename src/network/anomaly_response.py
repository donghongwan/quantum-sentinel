class AnomalyResponse:
    def __init__(self):
        self.responses = {
            "high": "Immediate action required: escalate to the security team.",
            "medium": "Monitor the situation closely and prepare a report.",
            "low": "No immediate action required, but keep an eye on the logs."
        }

    def generate_response(self, anomaly_level):
        """Generate an automated response based on the anomaly level."""
        return self.responses.get(anomaly_level, "Unknown anomaly level.")

if __name__ == "__main__":
    # Example usage
    anomaly_response = AnomalyResponse()
    anomaly_level = "high"  # This would be determined by your anomaly detection system
    response = anomaly_response.generate_response(anomaly_level)
    print("Automated Response:", response)
