import functools
import time
from typing import Callable, Any, Dict

# Cache for computed results to avoid redundant calculations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for performance optimization via result caching."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(items: list, batch_size: int = 100) -> list:
    """Efficient generator for chunked data processing."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator for monitoring function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"Execution of {func.__name__} took {duration:.4f} seconds")
        return result
    return wrapper

def clear_cache() -> None:
    """Manual reset for memoization storage."""
    _memoization_cache.clear()