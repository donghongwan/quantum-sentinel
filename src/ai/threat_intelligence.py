import requests

class ThreatIntelligence:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_threat_data(self):
        """Fetch threat intelligence data from the API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data:", response.status_code)
            return None

    def analyze_threats(self, threat_data):
        """Analyze the fetched threat data."""
        # Placeholder for analysis logic
        for threat in threat_data:
            print(f"Threat: {threat['name']}, Severity: {threat['severity']}")

if __name__ == "__main__":
    threat_intel = ThreatIntelligence("https://api.threatintelligence.com/v1/threats")
    threat_data = threat_intel.fetch_threat_data()
    if threat_data:
        threat_intel.analyze_threats(threat_data)
