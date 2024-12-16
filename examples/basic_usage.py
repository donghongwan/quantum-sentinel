from logging.log_handler import CustomLogHandler
from logging.log_formatter import CustomLogFormatter
import logging

def basic_usage():
    logger = logging.getLogger('basic_usage_logger')
    logger.setLevel(logging.INFO)
    handler = CustomLogHandler('logs/basic_usage.log')
    handler.setFormatter(CustomLogFormatter())
    logger.addHandler(handler)

    logger.info("This is a basic usage example.")

if __name__ == "__main__":
    basic_usage()
