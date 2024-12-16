import os
import time

class LogRetention:
    """Log retention policies and management."""
    
    def __init__(self, log_directory, retention_period_days):
        self.log_directory = log_directory
        self.retention_period = retention_period_days * 86400  # Convert days to seconds

    def clean_old_logs(self):
        """Remove logs older than the retention period."""
        current_time = time.time()
        for filename in os.listdir(self.log_directory):
            file_path = os.path.join(self.log_directory, filename)
            if os.path.isfile(file_path):
                file_age = current_time - os.path.getmtime(file_path)
                if file_age > self.retention_period:
                    os.remove(file_path)
                    print(f"Deleted old log file: {file_path}")

if __name__ == "__main__":
    # Example usage
    log_retention = LogRetention('logs', retention_period_days=30)
    log_retention.clean_old_logs()
