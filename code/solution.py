# Vance Vaughan - Assignment 3

# returns a formatted alert string
def format_alert(severity, source_ip, alert_message):
    return f"[{severity}] - {source_ip}: {alert_message}"