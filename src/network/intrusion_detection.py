import os
import time

class IntrusionDetection:
    def __init__(self, log_file='/var/log/auth.log'):
        self.log_file = log_file

    def monitor_logs(self):
        """Monitor log files for suspicious activity."""
        print(f"Monitoring {self.log_file} for suspicious activity...")
        with open(self.log_file, 'r') as file:
            file.seek(0, os.SEEK_END)  # Move to the end of the file
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)  # Sleep briefly
                    continue
                self.process_line(line)

    def process_line(self, line):
        """Process each line of the log file."""
        if "Failed password" in line:
            print("Suspicious activity detected:", line.strip())

if __name__ == "__main__":
    # Example usage
    ids = IntrusionDetection()
    ids.monitor_logs()
