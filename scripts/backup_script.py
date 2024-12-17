import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    """Backup files from source directory to backup directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    shutil.copytree(source_dir, backup_path)
    print(f"Backup of {source_dir} created at {backup_path}.")

if __name__ == "__main__":
    source_dir = "logs"  # Directory to backup
    backup_dir = "backups"  # Backup destination
    backup_files(source_dir, backup_dir)
