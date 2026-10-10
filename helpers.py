from typing import Any, Dict, List, Union

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary with concatenated keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_list(data: List[Any]) -> List[Any]:
    """Remove None values from a list."""
    return [item for item in data if item is not None]

def chunk_data(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into chunks of a given size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_get(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """Access nested dictionary keys safely."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data