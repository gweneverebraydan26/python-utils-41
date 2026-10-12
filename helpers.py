import os
import json
from typing import Any, Dict, Optional

def load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(data: Any, file_path: str) -> bool:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_filename(name: str) -> str:
    """Remove illegal characters from a filename string."""
    forbidden = '<>:"/\\|?*'
    return ''.join(c for c in name if c not in forbidden).strip()

def get_env_var(key: str, default: Any = None) -> Any:
    """Fetch environment variable with a default."""
    return os.environ.get(key, default)