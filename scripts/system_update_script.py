import os
import subprocess

def update_system():
    """Update system components."""
    print("Updating system components...")

    # Update package lists
    subprocess.run(["sudo", "apt-get", "update"])

    # Upgrade installed packages
    subprocess.run(["sudo", "apt-get", "upgrade", "-y"])

    # Clean up unnecessary packages
    subprocess.run(["sudo", "apt-get", "autoremove", "-y"])

    print("System update complete.")

if __name__ == "__main__":
    update_system()
