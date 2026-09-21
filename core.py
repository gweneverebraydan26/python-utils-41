from typing import Any, Iterable, Dict, List, Optional
from collections import defaultdict

def deep_flatten(items: Iterable[Any]) -> List[Any]:
    """Recursively flatten nested iterables into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def group_by_key(items: Iterable[Dict[Any, Any]], key: str) -> Dict[Any, List[Dict[Any, Any]]]:
    """Group a list of dictionaries by a common key value."""
    groups = defaultdict(list)
    for item in items:
        val = item.get(key)
        if val is not None:
            groups[val].append(item)
    return dict(groups)

def sanitize_dict(data: Dict[Any, Any], keys_to_remove: Optional[List[str]] = None) -> Dict[Any, Any]:
    """Return a new dictionary excluding specified keys."""
    if not keys_to_remove:
        return data.copy()
    return {k: v for k, v in data.items() if k not in keys_to_remove}

def safe_get(data: Dict[Any, Any], path: str, default: Any = None) -> Any:
    """Access nested dictionary values via dot notation path."""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError, AttributeError):
        return default