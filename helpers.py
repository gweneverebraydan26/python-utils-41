import os
import json
from typing import Any, Dict, Optional

def load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Serialize data to a JSON file with indentation."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.getenv(key, default or "")

def ensure_dir(directory: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flatten nested dictionary structures."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)