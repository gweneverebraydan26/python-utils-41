from typing import Any, List, Optional, Type, TypeVar

T = TypeVar("T")


def safe_get(target_dict: Any, keys: List[str], default: Optional[Any] = None) -> Any:
    """Safely retrieve nested values from a dictionary without raising exceptions."""
    if not isinstance(target_dict, dict):
        return default

    current = target_dict
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def safe_cast(val: Any, to_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    """Convert a value to a target type with graceful fallback on edge-case failures."""
    if val is None:
        return default

    try:
        return to_type(val)
    except (ValueError, TypeError, OverflowError):
        return default


def safe_truncate(text: Any, max_len: int, suffix: str = "...") -> str:
    """Truncate input to max length, handling non-string objects and invalid bounds."""
    if text is None:
        return ""

    str_val = str(text) if not isinstance(text, str) else text

    if max_len <= 0:
        return ""

    if len(str_val) <= max_len:
        return str_val

    if max_len <= len(suffix):
        return str_val[:max_len]

    return str_val[: max_len - len(suffix)] + suffix
