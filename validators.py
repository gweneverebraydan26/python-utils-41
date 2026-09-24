from typing import Any, Optional, Dict

def validate_data_schema(data: Any, schema: Dict[str, type]) -> bool:
    """Validates that a dictionary matches expected types."""
    if not isinstance(data, dict):
        return False

    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Returns value if not None, otherwise default."""
    return value if value is not None else default

def is_non_empty_string(value: Any) -> bool:
    """Checks if value is a string and not empty."""
    return isinstance(value, str) and len(value.strip()) > 0

def format_data_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null entries from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}