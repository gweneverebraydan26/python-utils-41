import functools
import time
from typing import Callable, Any, Dict

# Cache dictionary to store function results
_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Performance optimization for expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for memory-efficient batch processing of lists."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator to log execution time for performance profiling."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper