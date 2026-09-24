import json
import os
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Any, filepath: str) -> None:
    """Serializes data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_string(text: str) -> str:
    """Removes whitespace and converts to lowercase."""
    return str(text).strip().lower()

def ensure_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)