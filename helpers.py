import json
from typing import Any, Dict, Optional
from datetime import datetime

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Loads and parses a JSON file safely."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json_file(data: Dict[str, Any], file_path: str) -> bool:
    """Saves dictionary to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_timestamp() -> str:
    """Returns formatted ISO 8601 timestamp."""
    return datetime.now().isoformat()

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: list, size: int):
    """Splits a list into chunks of specific size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]