import numpy as np

class BehaviorAnalysis:
    def __init__(self):
        pass

    def analyze_behavior(self, user_data):
        """Analyze user behavior to detect anomalies."""
        # Placeholder for behavior analysis logic
        mean = np.mean(user_data)
        std_dev = np.std(user_data)
        anomalies = [data for data in user_data if abs(data - mean) > 2 * std_dev]
        return anomalies

if __name__ == "__main__":
    # Example usage
    ba = BehaviorAnalysis()
    user_data = [10, 12, 11, 13, 100, 12, 11]  # Example user behavior data
    anomalies = ba.analyze_behavior(user_data)
    print("Detected Anomalies:", anomalies)
