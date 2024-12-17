import requests
import json

def collect_training_data(api_endpoint, output_file):
    """Collect training data from a specified API endpoint."""
    response = requests.get(api_endpoint)
    
    if response.status_code == 200:
        with open(output_file, 'w') as f:
            json.dump(response.json(), f)
        print(f"Training data collected and saved to {output_file}.")
    else:
        print(f"Failed to collect data. Status code: {response.status_code}")

if __name__ == "__main__":
    api_endpoint = "http://localhost:5000/api/data"  # Replace with your actual API endpoint
    output_file = "data/training_data.json"
    collect_training_data(api_endpoint, output_file)
