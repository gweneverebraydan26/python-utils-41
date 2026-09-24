import json
from typing import Any, Dict, Optional

def safe_json_load(data: str, default: Optional[Dict] = None) -> Dict:
    """
    Safely parses a JSON string into a dictionary.
    Returns the default value if parsing fails.
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default if default is not None else {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single level.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none_values(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Removes keys with None values from a dictionary.
    """
    return {k: v for k, v in data.items() if v is not None}