import time
import logging

class LogMonitor:
    """Real-time log monitoring."""
    
    def __init__(self, log_file):
        self.log_file = log_file

    def tail(self, n=10):
        """Tail the last n lines of the log file."""
        with open(self.log_file, 'r') as f:
            lines = f.readlines()
            return lines[-n:]

    def monitor(self):
        """Monitor the log file for new entries."""
        with open(self.log_file, 'r') as f:
            f.seek(0, 2)  # Move to the end of the file
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)  # Sleep briefly
                    continue
                print(line.strip())  # Print new log entries

if __name__ == "__main__":
    # Example usage
    log_monitor = LogMonitor('app.log')
    print("Last 10 log entries:")
    print(log_monitor.tail(10))
    print("Monitoring new log entries:")
    log_monitor.monitor()
