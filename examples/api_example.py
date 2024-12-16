import requests

def api_example():
    response = requests.get('http://localhost:5000/api/endpoint')  # Replace with your actual API endpoint
    print("API Response:", response.json())

if __name__ == "__main__":
    api_example()
