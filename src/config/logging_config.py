import logging

def setup_logging(log_file='app.log'):
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

if __name__ == "__main__":
    # Example usage
    setup_logging()
    logging.info("Logging is set up.")
