from typing import Any, Optional, Dict, List

def validate_schema(data: Any, schema: Dict[str, type]) -> bool:
    """Verify that dictionary matches expected types."""
    if not isinstance(data, dict):
        return False
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Clean string input by stripping whitespace and handling None."""
    if isinstance(value, str):
        cleaned = value.strip()
        return cleaned if cleaned else default
    return value or default

def ensure_list(item: Any) -> List[Any]:
    """Wrap single item in list or return as is."""
    if item is None:
        return []
    return item if isinstance(item, list) else [item]

def is_non_empty_dict(data: Any) -> bool:
    """Check if variable is a non-empty dictionary."""
    return isinstance(data, dict) and len(data) > 0