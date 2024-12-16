import logging

class AuditTrail:
    """Audit trail for tracking changes and access."""
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('audit_logger')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_change(self, user, action, details):
        """Log a change made by a user."""
        self.logger.info(f"User: {user}, Action: {action}, Details: {details}")

if __name__ == "__main__":
    # Example usage
    audit_trail = AuditTrail('audit.log')
    audit_trail.log_change("admin", "UPDATE", "Updated user permissions.")
