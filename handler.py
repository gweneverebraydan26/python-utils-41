import json
import os
from typing import Any, Optional

def load_json(file_path: str) -> dict:
    """Safely load and parse a JSON file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: dict, file_path: str) -> None:
    """Serialize data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_var(key: str, default: Optional[Any] = None) -> Any:
    """Retrieve environment variable with default fallback."""
    return os.environ.get(key, default)

def chunk_list(data: list, size: int):
    """Split a list into chunks of defined size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Normalize and clean file path strings."""
    return os.path.normpath(path.strip())