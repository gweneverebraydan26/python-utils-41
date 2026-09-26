import functools
import itertools
from typing import Any, Callable, Dict, List, Sequence, Tuple


class FastDataProcessor:
    """Core processor optimized for batched memoized operations."""

    __slots__ = ('_cache', '_batch_size')

    def __init__(self, batch_size: int = 1000) -> None:
        self._batch_size = max(1, batch_size)
        self._cache: Dict[Tuple[Any, ...], Any] = {}

    def memoized_transform(self, func: Callable[..., Any], *args: Any) -> Any:
        """Executes function with fast dictionary caching based on arguments."""
        key = (func, args)
        if key not in self._cache:
            self._cache[key] = func(*args)
        return self._cache[key]

    def process_chunks(
        self, data: Sequence[Any], transform_fn: Callable[[Any], Any]
    ) -> List[Any]:
        """Transforms iterable data in optimized chunks to reduce memory footprint."""
        iterator = iter(data)
        results = []
        
        while True:
            chunk = list(itertools.islice(iterator, self._batch_size))
            if not chunk:
                break
            # Process chunk using list comprehension for optimized execution
            results.extend([transform_fn(item) for item in chunk])
            
        return results

    def clear_cache(self) -> None:
        """Purges internal performance cache."""
        self._cache.clear()
