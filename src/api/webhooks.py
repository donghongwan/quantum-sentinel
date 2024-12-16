from flask import request, jsonify

def handle_webhook(data):
    """Handle incoming webhook data."""
    # Process the webhook data here
    print("Webhook received:", data)
    return jsonify({"message": "Webhook processed"}), 200

def webhook_listener(f):
    """Decorator to handle webhook requests."""
    @wraps(f)
    def decorated(*args, **kwargs):
        data = request.json
        return handle_webhook(data)
    return decorated

if __name__ == "__main__":
    # Example usage
    print("Webhook module loaded.")
