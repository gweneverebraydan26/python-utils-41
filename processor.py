"""Data processing utility module for batching and transforming data streams."""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class DataProcessor:
    """Processes sequential data using custom transformation pipelines and batching logic."""

    def __init__(self, batch_size: int = 100) -> None:
        """Initialize the processor with a default batch size.

        Args:
            batch_size: Maximum number of items per processed batch.
        """
        if batch_size <= 0:
            raise ValueError("Batch size must be a positive integer.")
        self.batch_size: int = batch_size

    def chunk_data(self, items: List[T]) -> List[List[T]]:
        """Splits a list of items into chunks of specified batch size.

        Args:
            items: List of elements to split.

        Returns:
            List of lists containing chunked elements.
        """
        return [
            items[i : i + self.batch_size]
            for i in range(0, len(items), self.batch_size)
        ]

    def process_batch(
        self,
        items: List[T],
        transform: Callable[[T], R],
        predicate: Optional[Callable[[T], bool]] = None,
    ) -> List[R]:
        """Filters and transforms a collection of items.

        Args:
            items: Collection of items to process.
            transform: Function applied to each item.
            predicate: Optional filter condition. Items returning False are skipped.

        Returns:
            List of transformed values.
        """
        results: List[R] = []
        for item in items:
            if predicate is None or predicate(item):
                results.append(transform(item))
        return results

    def summarize(self, records: List[Dict[str, Any]], key: str) -> Dict[str, int]:
        """Aggregates occurrences of unique values for a specified dictionary key.

        Args:
            records: List of dictionary objects to inspect.
            key: The key whose values should be counted.

        Returns:
            Dictionary mapping key values to their frequency counts.
        """
        counts: Dict[str, int] = {}
        for record in records:
            if key in record:
                val_str = str(record[key])
                counts[val_str] = counts.get(val_str, 0) + 1
        return counts
