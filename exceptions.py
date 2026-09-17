class ValidationError(Exception):
    """Base exception for data validation failures."""
    pass

def validate_input(data, schema):
    """
    Validates dictionary input against expected keys and types.
    Ensures the data integrity before processing loop.
    """
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    for key, expected_type in schema.items():
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise ValidationError(
                f"Invalid type for {key}: expected {expected_type.__name__}, "
                f"got {type(data[key]).__name__}"
            )
    return True

def process_stream(items, schema):
    """
    Main processing loop with integrated input validation.
    """
    for index, item in enumerate(items):
        try:
            validate_input(item, schema)
            # Process item logic here
            print(f"Processing item {index}: {item}")
        except ValidationError as e:
            print(f"Skipping item {index} due to validation error: {e}")
            continue