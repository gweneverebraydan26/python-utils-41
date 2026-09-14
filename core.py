import functools
import time
from typing import Any, Callable, Dict

# Cache for repetitive computational tasks
_COMPUTATION_CACHE: Dict[str, Any] = {}

def memoize_result(func: Callable) -> Callable:
    """Decorator to cache expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
        if key not in _COMPUTATION_CACHE:
            _COMPUTATION_CACHE[key] = func(*args, **kwargs)
        return _COMPUTATION_CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Memory-efficient generator for large dataset batches."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceOptimizer:
    """Core utility for measuring and improving execution time."""
    @staticmethod
    def measure_execution(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"Execution time for {func.__name__}: {end - start:.4f}s")
            return result
        return wrapper