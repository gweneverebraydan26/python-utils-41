import functools
import time
from typing import Callable, Any, Dict

# Cache for performance optimization of expensive operations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

@memoize
def compute_heavy_data(n: int) -> int:
    """Simulates a resource-intensive computation task."""
    time.sleep(0.5)
    return sum(range(n))

class DataProcessor:
    """Handles high-throughput data processing operations."""
    def __init__(self, buffer_size: int = 1024):
        self.buffer_size = buffer_size
        self._cache = {}

    def process_stream(self, data: list) -> list:
        """Efficient batch processing using local cache."""
        results = []
        for item in data:
            if item not in self._cache:
                self._cache[item] = item * 2
            results.append(self._cache[item])
        return results