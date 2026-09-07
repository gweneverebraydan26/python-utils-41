import functools
import time
from typing import Callable, Any, Dict

# Cache to store function results for performance optimization
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching results of expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Generator for memory-efficient batch processing of large lists."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTimer:
    """Context manager for tracking block execution time."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start

def heavy_computation(n: int) -> int:
    """Simulated intensive task optimized by memoization."""
    result = 0
    for i in range(n):
        result += i**2
    return result