import json
from typing import Any, Dict, Optional
from pathlib import Path

def safe_json_load(file_path: str, default: Any = None) -> Any:
    """Reads json from file or returns default if file missing."""
    path = Path(file_path)
    if not path.exists():
        return default
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return default

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: list, chunk_size: int):
    """Generator for splitting lists into manageable chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def get_env_var_or_default(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieves environment variable with fallback value."""
    import os
    return os.environ.get(key, default)