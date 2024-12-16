import os
import subprocess

class FirewallManager:
    def __init__(self):
        pass

    def enable_firewall(self):
        """Enable the firewall."""
        print("Enabling firewall...")
        subprocess.run(["sudo", "ufw", "enable"])

    def disable_firewall(self):
        """Disable the firewall."""
        print("Disabling firewall...")
        subprocess.run(["sudo", "ufw", "disable"])

    def allow_port(self, port):
        """Allow traffic on a specific port."""
        print(f"Allowing traffic on port {port}...")
        subprocess.run(["sudo", "ufw", "allow", str(port)])

    def deny_port(self, port):
        """Deny traffic on a specific port."""
        print(f"Denying traffic on port {port}...")
        subprocess.run(["sudo", "ufw", "deny", str(port)])

    def status(self):
        """Check the status of the firewall."""
        print("Checking firewall status...")
        subprocess.run(["sudo", "ufw", "status"])

if __name__ == "__main__":
    # Example usage
    fm = FirewallManager()
    fm.status()
    # Uncomment the following lines to enable/disable the firewall or modify rules
    # fm.enable_firewall()
    # fm.allow_port(22)  # Allow SSH
    # fm.deny_port(80)   # Deny HTTP
