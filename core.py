from typing import Any, Dict, List, Optional, Union

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges two configuration dictionaries.

    Args:
        base: The primary configuration dictionary.
        override: The dictionary containing updates.

    Returns:
        A new dictionary with merged values.
    """
    merged = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value
    return merged

def format_data(items: List[Union[str, int]], delimiter: str = ", ") -> str:
    """Converts a list of data to a joined string.

    Args:
        items: A list of string or integer values.
        delimiter: Separator used for joining elements.

    Returns:
        A string representation of the list contents.
    """
    return delimiter.join(str(i) for i in items)

def get_nested(data: Dict[str, Any], path: List[str], default: Any = None) -> Any:
    """Retrieves a value from a nested dictionary structure.

    Args:
        data: The dictionary to traverse.
        path: A list of keys representing the path.
        default: Value to return if path is missing.

    Returns:
        The value found at the path or the default.
    """
    current = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current