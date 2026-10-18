import functools
import time
from typing import Callable, Any, Dict

# Cache for expensive function calls to improve performance
_MEMOIZATION_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache results of deterministic functions."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _MEMOIZATION_CACHE:
            _MEMOIZATION_CACHE[key] = func(*args, **kwargs)
        return _MEMOIZATION_CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Generator for processing data in chunks to optimize memory."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for tracking code block execution duration."""
    def __init__(self, name: str):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.perf_counter() - self.start
        print(f"[PERF] {self.name} took {duration:.4f} seconds")