def conduct_threat_modeling():
    """Conduct a basic threat modeling exercise."""
    threats = [
        {"threat": "Unauthorized Access", "impact": "High", "likelihood": "Medium"},
        {"threat": "Data Breach", "impact": "Critical", "likelihood": "Low"},
        {"threat": "Denial of Service", "impact": "Medium", "likelihood": "High"},
    ]

    print("Threat Modeling Report:")
    for threat in threats:
        print(f"Threat: {threat['threat']}, Impact: {threat['impact']}, Likelihood: {threat['likelihood']}")

if __name__ == "__main__":
    conduct_threat_modeling()
