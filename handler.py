"""General utility handlers and helper functions."""

import time
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")


def safe_get(data: dict, keys: str, default: Any = None) -> Any:
    """Retrieve nested value from a dictionary using dot notation."""
    current = data
    for key in keys.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> List[List[T]]:
    """Split an iterable into chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    items = list(iterable)
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def retry_operation(
    func: Callable[[], T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,),
) -> T:
    """Retry a function call with exponential backoff."""
    attempt = 0
    current_delay = delay
    while attempt < retries:
        try:
            return func()
        except exceptions as err:
            attempt += 1
            if attempt >= retries:
                raise err
            time.sleep(current_delay)
            current_delay *= backoff


def parse_boolean(val: Any, default: bool = False) -> bool:
    """Convert string or numeric representations to boolean."""
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    if isinstance(val, str):
        cleaned = val.strip().lower()
        if cleaned in ("true", "1", "yes", "y", "on", "t"):
            return True
        if cleaned in ("false", "0", "no", "n", "off", "f"):
            return False
    return default
