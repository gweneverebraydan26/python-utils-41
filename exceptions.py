class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input(data, schema):
    """
    Validates dictionary input against expected keys and types.
    
    Args:
        data: The input dictionary to validate.
        schema: A dict mapping keys to expected types.
    
    Raises:
        ValidationError: If key is missing or type mismatch occurs.
    """
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")

    for key, expected_type in schema.items():
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise ValidationError(f"Key {key} expects {expected_type.__name__}")

def process_data(payload):
    """
    Main processing loop entry point with validation.
    """
    schema = {"id": int, "value": str}
    try:
        validate_input(payload, schema)
        # Process logic goes here
        return True
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return False