import pandas as pd
import matplotlib.pyplot as plt

class LogVisualization:
    """Visualization tools for log data."""
    
    def __init__(self, log_file):
        self.log_file = log_file

    def visualize_log_data(self):
        """Visualize log data."""
        # Load logs into a DataFrame (assuming CSV format for simplicity)
        logs = pd.read_csv(self.log_file)
        
        # Example visualization: Count of log levels
        log_counts = logs['level'].value_counts()
        log_counts.plot(kind='bar')
        plt.title('Log Level Counts')
        plt.xlabel('Log Level')
        plt.ylabel('Count')
        plt.show()

if __name__ == "__main__":
    # Example usage
    log_visualization = LogVisualization('logs/app.log')
    log_visualization.visualize_log_data()
