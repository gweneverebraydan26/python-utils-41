import os
import json
from typing import Any, Optional

def ensure_dir(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def load_json(filepath: str) -> Any:
    """Safely loads JSON from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json(filepath: str, data: Any) -> None:
    """Writes data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Fetches environment variable with fallback."""
    return os.environ.get(key, default)

def flatten_list(nested_list: list) -> list:
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def chunk_list(data: list, size: int) -> list:
    """Splits a list into smaller chunks."""
    return [data[i:i + size] for i in range(0, len(data), size)]