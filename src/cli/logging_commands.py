import logging

class LoggingCommands:
    def __init__(self, log_file='app.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def set_log_level(self, level):
        """Set the logging level."""
        level = level.upper()
        if level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            self.logger.setLevel(getattr(logging, level))
            print(f"Log level set to {level}.")
        else:
            print("Invalid log level. Use DEBUG, INFO, WARNING, ERROR, or CRITICAL.")

    def log_message(self, message):
        """Log a message at INFO level."""
        self.logger.info(message)
        print(f"Logged message: {message}")

if __name__ == "__main__":
    # Example usage
    logging_commands = LoggingCommands()
    logging_commands.set_log_level('DEBUG')
    logging_commands.log_message("This is a test log message.")
