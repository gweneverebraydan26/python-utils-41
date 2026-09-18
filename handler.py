import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure logger for performance monitoring
logger = logging.getLogger('python-utils-41')

_memoization_cache: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Cache function results to reduce redundant computation."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{tuple(sorted(kwargs.items()))}"
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class PerformanceHandler:
    """Utility class for performance-critical execution patterns."""
    
    @staticmethod
    def batch_process(items: list, chunk_size: int = 100) -> list:
        """Process items in memory-efficient generator chunks."""
        for i in range(0, len(items), chunk_size):
            yield items[i:i + chunk_size]

    @staticmethod
    def timed_execution(func: Callable) -> Callable:
        """Decorator for logging execution time of core tasks."""
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            logger.debug(f"execution of {func.__name__} took {duration:.4f}s")
            return result
        return wrapper

    @staticmethod
    def clear_cache() -> None:
        """Reset global memoization storage."""
        _memoization_cache.clear()