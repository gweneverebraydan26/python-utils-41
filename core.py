import functools
import time
from typing import Callable, Any, Dict

# global cache for heavy computation results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """decorator for caching expensive function calls"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 1000):
    """generator for memory-efficient data chunking"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """context manager for execution time profiling"""
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.label}] execution time: {elapsed:.6f}s")