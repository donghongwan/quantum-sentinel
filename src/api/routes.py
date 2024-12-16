from flask import Blueprint, jsonify, request

api_routes = Blueprint('api', __name__)

@api_routes.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200

@api_routes.route('/data', methods=['POST'])
def create_data():
    """Endpoint to create new data."""
    data = request.json
    # Here you would typically save the data to a database
    return jsonify({"message": "Data created", "data": data}), 201

@api_routes.route('/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    """Endpoint to retrieve data by ID."""
    # Here you would typically retrieve the data from a database
    return jsonify({"data_id": data_id, "data": "Sample data"}), 200

@api_routes.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    """Endpoint to delete data by ID."""
    # Here you would typically delete the data from a database
    return jsonify({"message": f"Data with ID {data_id} deleted"}), 204
