"""General utility functions for data manipulation and formatting."""

import re
from typing import Any, Dict, List, Optional


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def flatten_iterable(items: List[Any]) -> List[Any]:
    """Flatten arbitrarily nested lists or tuples into a single list."""
    flat_list = []
    for item in items:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten_iterable(list(item)))
        else:
            flat_list.append(item)
    return flat_list


def safe_cast(val: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Safely cast a value to a given type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate a string to a max length and append suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)].rstrip() + suffix


def sanitize_key(key: str) -> str:
    """Sanitize a string to be used as a clean variable or dict key."""
    clean = re.sub(r"[^\w\s-]", "", key).strip().lower()
    return re.sub(r"[-\s]+", "_", clean)
