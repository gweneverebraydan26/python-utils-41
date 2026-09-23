import json
import os
from typing import Any, Dict, Optional

def ensure_directory(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def load_json(file_path: str) -> Dict[str, Any]:
    """Loads and parses a JSON file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Writes dictionary data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with optional default."""
    return os.getenv(key, default or "")

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a flat one."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)