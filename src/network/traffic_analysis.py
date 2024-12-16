import pandas as pd
import matplotlib.pyplot as plt

class TrafficAnalysis:
    def __init__(self, log_file):
        self.log_file = log_file

    def load_data(self):
        """Load traffic data from a log file."""
        self.data = pd.read_csv(self.log_file)
        print("Data loaded successfully.")

    def analyze_traffic(self):
        """Analyze traffic patterns."""
        print("Analyzing traffic patterns...")
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        self.data.set_index('timestamp', inplace=True)
        self.data['bytes'].plot(title='Traffic Analysis', figsize=(10, 5))
        plt.xlabel('Time')
        plt.ylabel('Bytes')
        plt.show()

if __name__ == "__main__":
    # Example usage
    log_file = "traffic_log.csv"  # Change to your traffic log file
    traffic_analysis = TrafficAnalysis(log_file)
    traffic_analysis.load_data()
    traffic_analysis.analyze_traffic()
