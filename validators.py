class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input(data: dict, required_keys: list):
    """
    Ensures input dictionary contains all required keys and values.
    Raises ValidationError if validation fails.
    """
    if not isinstance(data, dict):
        raise ValidationError("input must be a dictionary")

    for key in required_keys:
        if key not in data:
            raise ValidationError(f"missing required key: {key}")
        if data[key] is None:
            raise ValidationError(f"value for {key} cannot be null")

def process_data(data: dict):
    """
    Main processing loop entry point with validation.
    """
    required = ["id", "payload"]
    try:
        validate_input(data, required)
        # Logic for processing valid data
        result = f"processed_{data['id']}"
        return result
    except ValidationError as e:
        # Log error and return failure status
        print(f"Validation failed: {e}")
        return None