from flask import request, jsonify
from marshmallow import Schema, fields, ValidationError

class DataSchema(Schema):
    """Schema for validating incoming data."""
    name = fields.Str(required=True)
    value = fields.Int(required=True)

def validate_data(data):
    """Validate incoming data against the schema."""
    schema = DataSchema()
    try:
        schema.load(data)
    except ValidationError as err:
        return err.messages
    return None

def validate_request(f):
    """Decorator to validate incoming requests."""
    @wraps(f)
    def decorated(*args, **kwargs):
        errors = validate_data(request.json)
        if errors:
            return jsonify({"errors": errors}), 400
        return f(*args, **kwargs)
    return decorated

if __name__ == "__main__":
    # Example usage
    sample_data = {"name": "example", "value": 42}
    print(validate_data(sample_data))  # Should return None if valid
