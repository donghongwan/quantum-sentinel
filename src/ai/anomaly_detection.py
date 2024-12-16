import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetection:
    def __init__(self, contamination=0.1):
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination)

    def fit(self, data):
        """Fit the model to the data."""
        self.model.fit(data)

    def predict(self, data):
        """Predict anomalies in the data."""
        predictions = self.model.predict(data)
        # Convert predictions: -1 for anomalies, 1 for normal points
        return [1 if pred == -1 else 0 for pred in predictions]

if __name__ == "__main__":
    # Example usage
    data = np.array([[1, 2], [2, 3], [1, 1], [10, 10], [2, 2], [3, 3]])
    anomaly_detector = AnomalyDetection(contamination=0.2)
    anomaly_detector.fit(data)
    predictions = anomaly_detector.predict(data)
    print("Predictions (1: anomaly, 0: normal):", predictions)
