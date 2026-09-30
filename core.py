import collections.abc
from typing import Any, Dict, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_nested(data: Dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    """Access nested dictionary values using dot-notation strings."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, TypeError):
        return default

def sanitize_keys(data: Dict[str, Any], prefix: str = 'clean_') -> Dict[str, Any]:
    """Ensure dictionary keys are string-prefixed for serialization safety."""
    return {f"{prefix}{k}": v for k, v in data.items()}