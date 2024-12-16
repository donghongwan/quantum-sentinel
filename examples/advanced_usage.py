from alerting.alerting import Alerting
from alerting.audit_trail import AuditTrail

def advanced_usage():
    alert_system = Alerting(alert_threshold=5)
    audit_trail = AuditTrail('logs/advanced_audit.log')

    audit_trail.log_change("admin", "UPDATE", "Updated user permissions.")
    alert_system.send_alert("User permissions updated.")

if __name__ == "__main__":
    advanced_usage()
