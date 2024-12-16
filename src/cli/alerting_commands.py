class AlertingCommands:
    def set_alert(self, alert_type, threshold):
        """Set an alert for a specific condition."""
        print(f"Alert set for {alert_type} when it exceeds {threshold}.")

    def check_alerts(self):
        """Check current alerts."""
        print("Checking current alerts... (This is a placeholder for actual alert checking logic)")

if __name__ == "__main__":
    # Example usage
    alerting_commands = AlertingCommands()
    alerting_commands.set_alert("CPU Usage", 80)
    alerting_commands.check_alerts()
