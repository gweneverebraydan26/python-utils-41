from typing import Any, Dict, List, Union


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i:i + size] for i in range(0, len(data), size)]


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary using a separator."""
    items: List[tuple] = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_get(data: Union[Dict[str, Any], List[Any]], path: str, default: Any = None) -> Any:
    """Safely retrieve nested dictionary or list value using dot notation."""
    keys = path.replace("[", ".").replace("]", "").split(".")
    current = data
    
    for key in keys:
        if not key:
            continue
        try:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list):
                current = current[int(key)]
            else:
                return default
        except (KeyError, IndexError, ValueError, TypeError):
            return default
            
    return current
