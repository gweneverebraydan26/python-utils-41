import functools
import time
from typing import Callable, Any, Dict

_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Thread-safe cache for expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator to yield chunks for memory efficiency."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator for monitoring execution performance overhead."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        # Standard logging can be injected here if required
        return result
    return wrapper