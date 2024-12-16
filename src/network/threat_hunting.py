import os
import time

class ThreatHunting:
    def __init__(self, log_directory):
        self.log_directory = log_directory

    def hunt_threats(self):
        """Proactively hunt for threats in log files."""
        print(f"Hunting for threats in {self.log_directory}...")
        while True:
            for filename in os.listdir(self.log_directory):
                if filename.endswith(".log"):
                    self.process_log_file(os.path.join(self.log_directory, filename))
            time.sleep(60)  # Check logs every minute

    def process_log_file(self, file_path):
        """Process a single log file for suspicious activity."""
        with open(file_path, 'r') as file:
            for line in file:
                if "unauthorized" in line or "failed login" in line:
                    print(f"Threat detected in {file_path}: {line.strip()}")

if __name__ == "__main__":
    # Example usage
    log_dir = "/var/log/security"  # Change to your log directory
    threat_hunter = ThreatHunting(log_dir)
    threat_hunter.hunt_threats()
