from typing import Any, Dict, Generator, List

def deep_merge(dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges two dictionaries, with dict_b taking precedence."""
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def chunk_iterable(items: List[Any], size: int) -> Generator[List[Any], None, None]:
    """Yields successive chunks of a specified size from the input list."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(items), size):
        yield items[i : i + size]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary, joining keys with a separator."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
