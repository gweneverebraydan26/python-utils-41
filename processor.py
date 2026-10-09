import functools
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    """Efficient batch processing pipeline with optimized chunking and memoization."""

    def __init__(self, batch_size: int = 1000) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size

    def chunk_stream(self, items: Iterable[T]) -> Iterable[List[T]]:
        """Yield successive chunks from an iterable to reduce memory overhead."""
        chunk: List[T] = []
        for item in items:
            chunk.append(item)
            if len(chunk) >= self.batch_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

    def process_batch(self, items: Iterable[T], transform: Callable[[T], R]) -> List[R]:
        """Process items in batch streams applying transform efficiently."""
        results: List[R] = []
        for chunk in self.chunk_stream(items):
            results.extend(map(transform, chunk))
        return results


@functools.lru_cache(maxsize=1024)
def cached_transform(value: str) -> str:
    """Cached string transformation for repeated lookups."""
    return value.strip().lower()
