import os
import json
from typing import Any, List, Dict, Optional
from datetime import datetime

def read_file(filepath: str) -> Optional[str]:
    """Read file content safely, return None on error."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except (IOError, OSError):
        return None

def write_file(filepath: str, content: str) -> bool:
    """Write content to file, return True on success."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except (IOError, OSError):
        return False

def flatten_list(items: List[Any]) -> List[Any]:
    """Flatten a nested list into a single list."""
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of given size."""
    if size <= 0:
        return []
    return [items[i:i + size] for i in range(0, len(items), size)]

def get_file_extension(filename: str) -> str:
    """Return the file extension including dot."""
    return os.path.splitext(filename)[1]

def parse_json(data: str) -> Optional[Dict[str, Any]]:
    """Parse JSON string safely, return None on error."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return None

def get_timestamp() -> str:
    """Return current timestamp as ISO string."""
    return datetime.now().isoformat()

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, second overrides first."""
    result = dict1.copy()
    result.update(dict2)
    return result

def remove_duplicates(items: List[Any]) -> List[Any]:
    """Remove duplicate items preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result