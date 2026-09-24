import functools
import time
import collections
from typing import Callable, Any, Dict

# Cache implementation for performance optimization
# Stores function results to avoid redundant computations
_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def batch_process(data: list, size: int = 100):
    """Generator for efficient chunking of large datasets"""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def timed_execution(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Function {func.__name__} executed in {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Manual memory management for internal caches"""
    _cache.clear()