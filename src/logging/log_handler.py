import logging

class CustomLogHandler(logging.Handler):
    """Custom log handler to send logs to a specific destination."""
    
    def __init__(self, destination):
        super().__init__()
        self.destination = destination  # Could be a file, a database, etc.

    def emit(self, record):
        """Emit a log record to the specified destination."""
        log_entry = self.format(record)
        # Here you can implement the logic to send the log_entry to the destination
        # For example, writing to a file:
        with open(self.destination, 'a') as f:
            f.write(log_entry + '\n')

if __name__ == "__main__":
    # Example usage
    logger = logging.getLogger('custom_logger')
    logger.setLevel(logging.INFO)
    handler = CustomLogHandler('app.log')
    logger.addHandler(handler)
    logger.info("This is a test log entry.")
