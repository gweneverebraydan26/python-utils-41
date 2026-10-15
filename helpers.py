import json
import os
from typing import Any, Dict, Optional

def read_json_file(path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def ensure_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default or "")

def slugify(text: str) -> str:
    """Converts text to URL-friendly slug."""
    return "-".join(text.lower().split()).replace(" ", "-")

def chunk_list(data: list, size: int):
    """Yields successive n-sized chunks from list."""
    for i in range(0, len(data), size):
        yield data[i:i + size]