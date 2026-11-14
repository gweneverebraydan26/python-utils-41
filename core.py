"""Core execution engine with performance optimizations for data processing."""

import itertools
from functools import lru_cache
from typing import Any, Callable, Generator, Iterable, Sequence


class FastTaskRunner:
    """Optimized task wrapper utilizing slots and caching for fast computation."""

    __slots__ = ("_func", "_cache_size")

    def __init__(self, func: Callable[..., Any], cache_size: int = 256) -> None:
        self._func = lru_cache(maxsize=cache_size)(func)
        self._cache_size = cache_size

    def run(self, *args: Any) -> Any:
        """Execute underlying function with argument caching."""
        return self._func(*args)

    def clear_cache(self) -> None:
        """Clear memoized return values."""
        self._func.cache_clear()


def batch_iterable(
    iterable: Iterable[Any], chunk_size: int = 100
) -> Generator[list[Any], None, None]:
    """Yield items in chunks using memory-efficient iterator slicing."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")

    iterator = iter(iterable)
    while True:
        chunk = list(itertools.islice(iterator, chunk_size))
        if not chunk:
            break
        yield chunk


def fast_unique(items: Sequence[Any]) -> list[Any]:
    """Preserve element order while deduplicating in linear time."""
    return list(dict.fromkeys(items))
