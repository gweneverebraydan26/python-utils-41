"""Core execution engine with performance optimizations for batch processing."""

from typing import Any, Callable, Generator, TypeVar
import functools
import itertools

T = TypeVar("T")
R = TypeVar("R")


class FastBatchProcessor:
    """Optimized batch processing engine using slots and memory-efficient iterators."""

    __slots__ = ("batch_size", "_cache_size")

    def __init__(self, batch_size: int = 1000, cache_size: int = 2048) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size
        self._cache_size = cache_size

    def chunk_iterable(self, iterable: list[T]) -> Generator[list[T], None, None]:
        """Yield successive chunks from iterable without allocating full copies."""
        it = iter(iterable)
        while True:
            chunk = list(itertools.islice(it, self.batch_size))
            if not chunk:
                break
            yield chunk

    def process_batch(self, items: list[T], func: Callable[[T], R]) -> list[R]:
        """Execute function over items using built-in C-optimized map layout."""
        return list(map(func, items))

    @functools.lru_cache(maxsize=4096)
    def cached_eval(self, func: Callable[..., R], *args: Any) -> R:
        """Memoize repeated expensive function calls across data streams."""
        return func(*args)

    def run_pipeline(self, stream: list[T], steps: list[Callable[[Any], Any]]) -> list[Any]:
        """Execute a composed transformation pipeline over chunked streams."""
        if not steps:
            return stream

        # Compose step pipeline into a single call per item to minimize loop overhead
        def _composite_transform(item: Any) -> Any:
            val = item
            for step in steps:
                val = step(val)
            return val

        results: list[Any] = []
        for batch in self.chunk_iterable(stream):
            results.extend(self.process_batch(batch, _composite_transform))
        return results
