import json

def check_compliance(data_file, compliance_criteria):
    """Check compliance of data against specified criteria."""
    with open(data_file, 'r') as f:
        data = json.load(f)

    compliant = True
    for criterion in compliance_criteria:
        if criterion not in data:
            compliant = False
            print(f"Compliance check failed: {criterion} not found in data.")

    if compliant:
        print("All compliance checks passed.")
    else:
        print("Some compliance checks failed.")

if __name__ == "__main__":
    data_file = "data/user_data.json"  # Replace with your actual data file
    compliance_criteria = ["name", "email", "age"]  # Define your compliance criteria
    check_compliance(data_file, compliance_criteria)
