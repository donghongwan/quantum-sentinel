import os
import datetime

class NetworkForensics:
    def __init__(self, log_directory):
        self.log_directory = log_directory

    def analyze_logs(self):
        """Analyze network logs for suspicious activity."""
        print(f"Analyzing logs in {self.log_directory}...")
        for filename in os.listdir(self.log_directory):
            if filename.endswith(".log"):
                self.process_log_file(os.path.join(self.log_directory, filename))

    def process_log_file(self, file_path):
        """Process a single log file."""
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line or "WARNING" in line:
                    print(f"Suspicious activity found in {file_path}: {line.strip()}")

if __name__ == "__main__":
    # Example usage
    log_dir = "/var/log/network"  # Change to your log directory
    forensic_tool = NetworkForensics(log_dir)
    forensic_tool.analyze_logs()
