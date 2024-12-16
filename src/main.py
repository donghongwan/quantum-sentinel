import logging
from logging.log_handler import CustomLogHandler
from logging.log_formatter import CustomLogFormatter
from logging.log_monitor import LogMonitor
from alerting.alerting import Alerting
from alerting.audit_trail import AuditTrail
from alerting.log_analysis import LogAnalysis
from alerting.anomaly_detection_logs import AnomalyDetectionLogs
from log_management.log_retention import LogRetention
from log_management.log_encryption import LogEncryption
from log_management.log_aggregation import LogAggregation
from log_management.log_visualization import LogVisualization

def setup_logging():
    """Set up logging configuration."""
    logger = logging.getLogger('main_logger')
    logger.setLevel(logging.INFO)
    handler = CustomLogHandler('logs/app.log')
    handler.setFormatter(CustomLogFormatter())
    logger.addHandler(handler)
    return logger

def main():
    """Main application entry point."""
    logger = setup_logging()
    
    # Example usage of logging
    logger.info("Application started.")

    # Initialize components
    alert_system = Alerting(alert_threshold=5)
    audit_trail = AuditTrail('logs/audit.log')
    anomaly_logger = AnomalyDetectionLogs('logs/anomalies.log')
    
    # Log an example change
    audit_trail.log_change("admin", "CREATE", "Created a new user.")
    
    # Log an example anomaly
    anomaly_logger.log_anomaly("Unauthorized Access", "Detected access attempt from unknown IP.")
    
    # Log retention management
    log_retention = LogRetention('logs', retention_period_days=30)
    log_retention.clean_old_logs()
    
    # Log encryption example
    key = LogEncryption.generate_key()  # Generate a new key
    log_encryption = LogEncryption(key)
    encrypted_log = log_encryption.encrypt_log("Sensitive log entry.")
    logger.info(f"Encrypted Log: {encrypted_log}")
    
    # Log aggregation example
    log_aggregation = LogAggregation(['logs/app.log', 'logs/system.log'], 'logs/aggregated_logs.log')
    log_aggregation.aggregate_logs()
    
    # Log visualization example
    log_visualization = LogVisualization('logs/app.log')
    log_visualization.visualize_log_data()

    # Monitor logs in real-time (this will block, so you may want to run it in a separate thread)
    log_monitor = LogMonitor('logs/app.log')
    print("Monitoring new log entries:")
    log_monitor.monitor()

if __name__ == "__main__":
    main()
