"""General utility helpers for common data manipulation tasks."""

from typing import Any, Dict, Iterable, List, Optional, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> List[List[T]]:
    """Splits an iterable into list chunks of a specified maximum size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    items = list(iterable)
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges dict2 into dict1 without mutating input dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def safe_cast(val: Any, target_type: type, default: Optional[Any] = None) -> Any:
    """Safely attempts to cast a value to a target type with a fallback default."""
    try:
        return target_type(val)
    except (ValueError, TypeError):
        return default


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncates text to max_length including the length of the suffix."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix
