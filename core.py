import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results to optimize execution speed
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching return values of expensive calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class BatchProcessor:
    """Processor class optimized for memory-efficient iteration."""
    def __init__(self, data: list, chunk_size: int = 100):
        self.data = data
        self.chunk_size = chunk_size

    def process_stream(self):
        """Yield chunks using a generator to reduce memory footprint."""
        for i in range(0, len(self.data), self.chunk_size):
            yield self.data[i : i + self.chunk_size]

def benchmark_execution(func: Callable):
    """Execution time tracking for performance diagnostics."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution of {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper