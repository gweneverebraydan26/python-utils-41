import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return default or {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return default or {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes a dictionary to a JSON file safely."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except IOError:
        return False

def sanitize_dict_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively ensures dictionary keys are strings."""
    return {
        str(k): (sanitize_dict_keys(v) if isinstance(v, dict) else v)
        for k, v in data.items()
    }

def flatten_data(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionary structures into a single level."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_data(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)