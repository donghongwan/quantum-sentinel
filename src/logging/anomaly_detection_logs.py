import logging

class AnomalyDetectionLogs:
    """Logs specifically for anomaly detection."""
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('anomaly_logger')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_anomaly(self, anomaly_type, description):
        """Log an anomaly detected in the system."""
        self.logger.info(f"Anomaly Type: {anomaly_type}, Description: {description}")

if __name__ == "__main__":
    # Example usage
    anomaly_logger = AnomalyDetectionLogs('anomalies.log')
    anomaly_logger.log_anomaly("Unauthorized Access", "Detected access attempt from unknown IP.")
