from flask import jsonify

def generate_api_docs():
    """Generate API documentation."""
    docs = {
        "version": "1.0",
        "endpoints": [
            {
                "path": "/health",
                "method": "GET",
                "description": "Health check endpoint."
            },
            {
                "path": "/data",
                "method": "POST",
                "description": "Create new data."
            },
            {
                "path": "/data/<int:data_id>",
                "method": "GET",
                "description": "Retrieve data by ID."
            },
            {
                "path": "/data/<int:data_id>",
                "method": "DELETE",
                "description": "Delete data by ID."
            }
        ]
    }
    return jsonify(docs)

if __name__ == "__main__":
    # Example usage
    print(generate_api_docs().get_data())  # Simulate generating API documentation
