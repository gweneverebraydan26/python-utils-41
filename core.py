import functools
import time
from typing import Callable, Any, Dict

# Cache for repetitive function results to improve performance
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Memory-efficient generator for large dataset handling."""
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]

class PerformanceTracker:
    """Context manager for tracking code execution duration."""
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.perf_counter() - self.start
        print(f"[PERF] {self.label}: {duration:.4f}s")