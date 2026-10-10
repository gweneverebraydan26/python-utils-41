import functools
import itertools
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class FastDataTransformer:
    """Core utility for fast sequence transformation and memoized evaluation."""

    __slots__ = ("_cache_size", "_transform_func")

    def __init__(self, transform_func: Callable[[Any], Any], cache_size: int = 1024):
        self._cache_size = cache_size
        # Memoize transformation function to speed up lookups on duplicate inputs
        self._transform_func = functools.lru_cache(maxsize=cache_size)(transform_func)

    def process_item(self, item: Any) -> Any:
        """Process a single item using the cached transformation logic."""
        return self._transform_func(item)

    def process_batch(self, items: Iterable[Any], chunk_size: int = 256) -> List[Any]:
        """Process items in memory-efficient chunks to minimize allocation overhead."""
        iterator = iter(items)
        results = []

        while True:
            chunk = list(itertools.islice(iterator, chunk_size))
            if not chunk:
                break
            results.extend(map(self._transform_func, chunk))

        return results

    def clear_cache(self) -> None:
        """Reset internal memoization cache statistics."""
        self._transform_func.cache_clear()

    def cache_info(self) -> functools._CacheInfo:
        """Return cache performance metrics for monitoring."""
        return self._transform_func.cache_info()
