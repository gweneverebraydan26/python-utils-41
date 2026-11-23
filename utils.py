"""General utility functions for data manipulation and safe casting."""

import itertools
from typing import Any, Dict, Iterable, List, TypeVar

T = TypeVar("T")


def safe_cast(val: Any, to_type: type, default: Any = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    if val is None:
        return default
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def deep_merge_dicts(base: Dict[Any, Any], update: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries into a new dictionary."""
    merged = base.copy()
    for key, value in update.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged


def chunk_iterable(iterable: Iterable[T], size: int) -> List[List[T]]:
    """Split an iterable into fixed-size chunks."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")

    iterator = iter(iterable)
    chunks = []
    while True:
        chunk = list(itertools.islice(iterator, size))
        if not chunk:
            break
        chunks.append(chunk)
    return chunks


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length including suffix if it exceeds length."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return text[:max_length]
    return text[: max_length - len(suffix)] + suffix
