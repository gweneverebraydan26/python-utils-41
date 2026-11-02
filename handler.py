import json
import os
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Loads data from a json file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Saves dictionary to a json file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def safe_get(data: Dict, key: str, default: Any = None) -> Any:
    """Retrieves value from dictionary safely."""
    return data.get(key, default)

def chunk_list(data: list, size: int):
    """Splits a list into chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Normalizes and cleans file paths."""
    return os.path.normpath(path.strip())

def format_byte_size(size: int) -> str:
    """Converts integer bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"