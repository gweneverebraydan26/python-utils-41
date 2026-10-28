from typing import Any, Dict, List, Optional

def validate_schema(data: Any, schema: Dict[str, type]) -> bool:
    """Verify that a dictionary matches expected types."""
    if not isinstance(data, dict):
        return False
    
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_list(items: List[Any], filter_none: bool = True) -> List[Any]:
    """Clean list by removing null or invalid items."""
    if filter_none:
        return [i for i in items if i is not None]
    return items

def ensure_list(value: Any) -> List[Any]:
    """Force data into a consistent list format."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def dict_get_nested(data: Dict, keys: List[str], default: Any = None) -> Any:
    """Retrieve nested dictionary values safely."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default