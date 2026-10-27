import functools
from typing import Callable, Any, Dict

# Cache for computed processor results to avoid redundant calculations
_RESULT_CACHE: Dict[tuple, Any] = {}

def memoize_process(func: Callable) -> Callable:
    """Decorator to cache results of expensive operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _RESULT_CACHE:
            _RESULT_CACHE[key] = func(*args, **kwargs)
        return _RESULT_CACHE[key]
    return wrapper

class DataProcessor:
    """Handles batch processing with performance-optimized lookups."""
    
    def __init__(self, data: list):
        self._data = data

    @memoize_process
    def transform_item(self, item: int) -> int:
        """Simulates a resource-intensive transformation."""
        result = item * item
        for i in range(1000):
            result += (i % 2)
        return result

    def process_all(self) -> list:
        """Executes transformation on internal data set."""
        return [self.transform_item(i) for i in self._data]

    def clear_cache(self) -> None:
        """Resets the memoization dictionary."""
        _RESULT_CACHE.clear()