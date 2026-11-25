import json
import os
from typing import Any, Dict, List, Optional

def load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default)

def format_dict_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert dictionary keys to lowercase."""
    return {str(k).lower(): v for k, v in data.items()}