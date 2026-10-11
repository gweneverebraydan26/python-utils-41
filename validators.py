from typing import Any, Optional, Dict

def validate_schema(data: Any, schema: Dict[str, type]) -> bool:
    """
    Validates that a dictionary matches the provided type schema.
    Returns True if valid, False otherwise.
    """
    if not isinstance(data, dict):
        return False

    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
            
    return True

def sanitize_input(value: Any) -> str:
    """
    Converts any input into a stripped, safe string.
    """
    if value is None:
        return ""
    return str(value).strip()

def get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """
    Retrieves nested dictionary values using dot notation.
    Example: get_nested(data, 'user.profile.id')
    """
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, AttributeError):
        return default