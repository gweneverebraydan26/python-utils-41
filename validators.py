import re

def validate_input_data(data: dict) -> bool:
    """
    Validates core dictionary structure and value types.
    Returns True if valid, raises ValueError otherwise.
    """
    required_keys = {'id', 'payload', 'timestamp'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        raise ValueError(f"Missing required keys: {required_keys - data.keys()}")
    
    # Validate ID format (alphanumeric string)
    if not isinstance(data['id'], str) or not re.match(r'^[a-zA-Z0-9_-]+$', data['id']):
        raise ValueError("Invalid ID format: must be alphanumeric string")
        
    # Validate payload length constraints
    if not isinstance(data['payload'], (str, list)) or len(str(data['payload'])) > 1024:
        raise ValueError("Payload exceeds size limits or invalid type")
        
    return True

def process_main_loop(items: list):
    """
    Example integration loop for data processing.
    """
    results = []
    for item in items:
        try:
            if validate_input_data(item):
                # Process logic here
                results.append(item['id'])
        except ValueError as e:
            print(f"Validation skipped item: {e}")
    return results