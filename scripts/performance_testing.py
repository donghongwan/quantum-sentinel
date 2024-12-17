import time
import requests

def performance_test(api_endpoint, iterations=100):
    """Test the performance of an API endpoint."""
    total_time = 0

    for i in range(iterations):
        start_time = time.time()
        response = requests.get(api_endpoint)
        end_time = time.time()

        total_time += (end_time - start_time)
        print(f"Iteration {i + 1}: Status Code: {response.status_code}, Time Taken: {end_time - start_time:.4f} seconds")

    average_time = total_time / iterations
    print(f"Average response time over {iterations} iterations: {average_time:.4f} seconds")

if __name__ == "__main__":
    api_endpoint = "http://localhost:5000/api/endpoint"  # Replace with your actual API endpoint
    performance_test(api_endpoint)
