import os
import shutil
from datetime import datetime

def rotate_logs(log_directory, backup_directory):
    """Rotate logs by moving old logs to a backup directory."""
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    for log_file in os.listdir(log_directory):
        if log_file.endswith(".log"):
            log_path = os.path.join(log_directory, log_file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(backup_directory, f"{log_file}_{timestamp}")
            shutil.move(log_path, backup_file)
            print(f"Rotated log: {log_file} to {backup_file}")

if __name__ == "__main__":
    log_directory = "logs"  # Directory containing logs
    backup_directory = "backups/logs"  # Backup directory for rotated logs
    rotate_logs(log_directory, backup_directory)
