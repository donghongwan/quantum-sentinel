import logging

class Alerting:
    """Alerting mechanisms for critical events."""
    
    def __init__(self, alert_threshold):
        self.alert_threshold = alert_threshold
        self.logger = logging.getLogger('alerting_logger')
        self.logger.setLevel(logging.WARNING)

    def send_alert(self, message):
        """Send an alert for critical events."""
        self.logger.warning(f"ALERT: {message}")
        # Here you can implement additional alerting mechanisms, e.g., email, SMS, etc.

if __name__ == "__main__":
    # Example usage
    alert_system = Alerting(alert_threshold=5)
    alert_system.send_alert("CPU usage exceeded threshold.")
