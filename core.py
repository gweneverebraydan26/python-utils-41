from typing import Any, Callable, Dict, Iterable, Iterator, List, TypeVar
import functools
import time

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Iterator[List[T]]:
    """Yield successive chunks of a given size from an iterable.

    Args:
        iterable: The sequence or iterable to split into chunks.
        chunk_size: The maximum size of each chunk.

    Yields:
        Lists containing elements from the iterable up to chunk_size.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into a single-level dictionary.

    Args:
        data: The dictionary to flatten.
        parent_key: Prefix for keys during recursion.
        sep: Separator character for joined keys.

    Returns:
        A flattened dictionary with concatenated keys.
    """
    items: Dict[str, Any] = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items


def retry_on_exception(
    max_attempts: int = 3,
    delay: float = 1.0,
    exceptions: tuple = (Exception,)
) -> Callable:
    """Decorator that retries a function if it raises specified exceptions.

    Args:
        max_attempts: Maximum number of execution attempts.
        delay: Delay in seconds between retries.
        exceptions: Tuple of exception classes to catch.

    Returns:
        Wrapped callable with retry behavior.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise err
                    time.sleep(delay)
        return wrapper
    return decorator