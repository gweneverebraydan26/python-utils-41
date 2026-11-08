import functools
import itertools
from typing import Any, Callable, Dict, List, Iterable, Generator


class FastBatchProcessor:
    """High-performance batch processing engine with memoization and stream lazy loading."""

    def __init__(self, batch_size: int = 100, max_cache_size: int = 1024):
        self.batch_size = max(1, batch_size)
        self.max_cache_size = max_cache_size
        self._cache: Dict[Any, Any] = {}

    def _chunk_stream(self, iterable: Iterable[Any]) -> Generator[List[Any], None, None]:
        """Yield successive batches from an iterable without full memory load."""
        iterator = iter(iterable)
        while batch := list(itertools.islice(iterator, self.batch_size)):
            yield batch

    def process_stream(self, items: Iterable[Any], transform_fn: Callable[[Any], Any]) -> Generator[Any, None, None]:
        """Process an incoming stream using chunking and cache lookups for speed."""
        cache = self._cache
        max_size = self.max_cache_size

        for batch in self._chunk_stream(items):
            for item in batch:
                if item not in cache:
                    if len(cache) >= max_size:
                        cache.clear()  # Fast flush on cache boundary
                    cache[item] = transform_fn(item)
                yield cache[item]

    def process_batch(self, items: List[Any], transform_fn: Callable[[Any], Any]) -> List[Any]:
        """Eagerly transform list of items returning pre-allocated results."""
        return list(self.process_stream(items, transform_fn))
