class ValidationError(Exception):
    """Base class for validation errors in processing."""
    pass

def validate_input_data(data: dict) -> None:
    """Ensures incoming data dictionary contains required keys."""
    required_keys = {'id', 'payload', 'timestamp'}
    
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    missing = required_keys - data.keys()
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

def run_processing_loop(items: list):
    """Main processing loop with data validation."""
    results = []
    for item in items:
        try:
            validate_input_data(item)
            # Mock business logic execution
            results.append({"status": "processed", "id": item.get("id")})
        except ValidationError as e:
            # Log error and continue with next item
            print(f"Validation failed for {item}: {e}")
            continue
    return results