from flask import Flask
from routes import api_routes
from middleware import request_logging

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Register middleware
    app.before_request(request_logging)

    # Register API routes
    app.register_blueprint(api_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
