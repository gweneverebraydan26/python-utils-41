from typing import List, Any, Optional

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Recursively flatten a nested list structure into a single list."""
    flat: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def get_nested_value(data: dict, keys: List[str], default: Any = None) -> Any:
    """Retrieve a value from a nested dictionary using a list of keys."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def chunk_iterable(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("chunk size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]