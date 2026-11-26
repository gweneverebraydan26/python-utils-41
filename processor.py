import functools
from typing import Callable, Any, Dict

# Cache for repetitive computational tasks
_memoization_cache: Dict[tuple, Any] = {}

def memoize_processor(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class DataProcessor:
    """High-performance batch processor for numeric datasets."""
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    @memoize_processor
    def transform(self, data: tuple) -> list:
        """Applies vectorized-style transformations to input sequences."""
        return [x * 2 if x > self.threshold else x / 2 for x in data]

    def batch_process(self, datasets: list[tuple]) -> list[list]:
        """Process list of tuples efficiently."""
        return [self.transform(ds) for ds in datasets]

def clear_processor_cache() -> None:
    """Manual memory reclamation for the cache."""
    _memoization_cache.clear()