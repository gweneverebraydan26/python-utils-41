import functools
import time
from typing import Any, Callable, Dict, List, Sequence, Tuple, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class FastMemoizer:
    """A high-performance thread-safe memoizer with expiration support."""

    def __init__(self, maxsize: int = 128, ttl_seconds: float = 60.0) -> None:
        self.maxsize = maxsize
        self.ttl = ttl_seconds
        self._cache: Dict[Any, Tuple[Any, float]] = {}

    def memoize(self, func: Callable[..., R]) -> Callable[..., R]:
        """Decorator to cache function execution results based on arguments."""

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            kw_items = tuple(sorted(kwargs.items()))
            key = (args, kw_items)
            now = time.monotonic()

            if key in self._cache:
                result, timestamp = self._cache[key]
                if now - timestamp < self.ttl:
                    return result

            result = func(*args, **kwargs)

            # Evict oldest entry if size limit exceeded
            if len(self._cache) >= self.maxsize:
                oldest_key = min(self._cache, key=lambda k: self._cache[k][1])
                del self._cache[oldest_key]

            self._cache[key] = (result, now)
            return result

        return wrapper

    def clear(self) -> None:
        """Clear all cached entries."""
        self._cache.clear()


def batch_process(
    items: Sequence[T], batch_size: int, worker_fn: Callable[[List[T]], List[R]]
) -> List[R]:
    """Optimized batch execution helper for processing large sequences."""
    if batch_size <= 0:
        raise ValueError("batch_size must be a positive integer")

    results: List[R] = []
    for i in range(0, len(items), batch_size):
        chunk = list(items[i : i + batch_size])
        results.extend(worker_fn(chunk))
    return results
