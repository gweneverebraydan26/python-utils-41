from typing import Any, Dict, List, Union
import collections.abc

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of a fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_get(data: Dict[str, Any], keys: str, default: Any = None) -> Any:
    """Retrieves nested dictionary values using dot notation."""
    for key in keys.split('.'):
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data