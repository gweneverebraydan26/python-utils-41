import json
from typing import Any, Dict, List, Optional
from pathlib import Path

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    path = Path(file_path)
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary into single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller balanced chunks."""
    if size <= 0:
        return [data]
    return [data[i:i + size] for i in range(0, len(data), size)]

def sanitize_string(text: str) -> str:
    """Remove non-alphanumeric characters from string."""
    return ''.join(c for c in text if c.isalnum() or c.isspace()).strip()