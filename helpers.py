import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads a JSON file and returns a dictionary."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.getenv(key, default) or ""

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks of fixed size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)