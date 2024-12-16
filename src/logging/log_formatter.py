import logging

class CustomLogFormatter(logging.Formatter):
    """Custom log formatter to format log messages."""
    
    def format(self, record):
        # Customize the log format here
        log_format = f'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)
        return formatter.format(record)

if __name__ == "__main__":
    # Example usage
    logger = logging.getLogger('formatted_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(CustomLogFormatter())
    logger.addHandler(handler)
    logger.info("This is a formatted log entry.")
