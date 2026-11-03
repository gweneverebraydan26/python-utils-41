from typing import Any, Iterable, Optional, TypeVar

T = TypeVar('T')

def flatten(items: Iterable[Any]) -> list[Any]:
    """Flatten a nested list structure into a single list."""
    result: list[Any] = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def get_first(items: Iterable[T], default: Optional[T] = None) -> Optional[T]:
    """Retrieve the first element of an iterable or return a default."""
    return next(iter(items), default)

def chunker(data: list[T], size: int) -> Iterable[list[T]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_invert(data: dict[Any, T]) -> dict[T, Any]:
    """Swap keys and values in a dictionary."""
    return {v: k for k, v in data.items()}
