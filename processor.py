import json
from typing import Any, Dict, List, Optional
from pathlib import Path

def load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    path = Path(file_path)
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i:i + size] for i in range(0, len(data), size)]

def slugify(text: str) -> str:
    """Convert string to a URL-friendly slug."""
    return "-".join(text.lower().split()).replace(" ", "-")

def get_nested(data: Dict, keys: List[str], default: Any = None) -> Any:
    """Retrieve nested dictionary values using a key list."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data