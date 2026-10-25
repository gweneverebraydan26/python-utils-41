import time
import functools
from typing import Any, Callable, Dict, Tuple, Optional


class TimedLRUCache:
    """An LRU cache implementation with time-to-live expiration."""

    def __init__(self, maxsize: int = 128, ttl: float = 60.0) -> None:
        self.maxsize = maxsize
        self.ttl = ttl
        self._cache: Dict[Any, Tuple[Any, float]] = {}

    def get(self, key: Any) -> Optional[Any]:
        if key not in self._cache:
            return None

        value, timestamp = self._cache[key]
        if time.time() - timestamp > self.ttl:
            del self._cache[key]
            return None

        return value

    def set(self, key: Any, value: Any) -> None:
        if len(self._cache) >= self.maxsize and key not in self._cache:
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        self._cache[key] = (value, time.time())

    def clear(self) -> None:
        self._cache.clear()


def memoize_ttl(ttl: float = 60.0, maxsize: int = 128) -> Callable:
    """Decorator to cache function execution results with time-based invalidation."""
    cache = TimedLRUCache(maxsize=maxsize, ttl=ttl)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            cached_result = cache.get(key)
            if cached_result is not None:
                return cached_result

            result = func(*args, **kwargs)
            cache.set(key, result)
            return result

        wrapper.cache_clear = cache.clear  # type: ignore
        return wrapper

    return decorator


class CoreProcessor:
    """High-performance batch processing core engine."""

    def __init__(self, batch_size: int = 100) -> None:
        self.batch_size = batch_size

    @memoize_ttl(ttl=300.0, maxsize=256)
    def compute_heavy_transform(self, item_id: str, value: float) -> float:
        """Simulates expensive transformation optimized with TTL caching."""
        return round((value ** 1.5) / 3.14159, 4)

    def process_batch(self, items: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Processes a sequence of payload items efficiently using caching."""
        results = []
        for item in items:
            transformed = self.compute_heavy_transform(
                item["id"], float(item["value"])
            )
            results.append({"id": item["id"], "result": transformed})
        return results
