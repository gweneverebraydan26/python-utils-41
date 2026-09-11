from typing import Any, Dict

def get_nested(data: Dict[str, Any], path: str, default: Any = None, separator: str = ".") -> Any:
    """
    Retrieve a value from a nested dictionary using a separator-delimited path.
    """
    if not path:
        return data
    
    keys = path.split(separator)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def set_nested(data: Dict[str, Any], path: str, value: Any, separator: str = ".") -> None:
    """
    Set a value in a nested dictionary using a separator-delimited path,
    creating intermediate dictionaries if they do not exist.
    """
    if not path:
        return
    
    keys = path.split(separator)
    current = data
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value
