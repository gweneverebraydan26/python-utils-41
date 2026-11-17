from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles batch processing of dictionary-based datasets."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        self.settings: Dict[str, Any] = settings or {}

    def transform(self, items: List[Dict[str, Any]], key: str, modifier: callable) -> List[Dict[str, Any]]:
        """
        Applies a modification function to values under a specific key.

        Args:
            items: A list of dictionaries to process.
            key: The key in each dictionary to transform.
            modifier: A function that returns a modified value.

        Returns:
            A new list containing updated dictionaries.
        """
        processed: List[Dict[str, Any]] = []
        for item in items:
            new_item = item.copy()
            if key in new_item:
                new_item[key] = modifier(new_item[key])
            processed.append(new_item)
        return processed

    def filter_by_threshold(self, items: List[Dict[str, int]], key: str, threshold: int) -> List[Dict[str, int]]:
        """
        Filters items based on an integer value threshold.

        Args:
            items: List of dictionaries containing integers.
            key: Key used for comparison.
            threshold: The minimum value required to keep an item.

        Returns:
            A filtered list of items.
        """
        return [item for item in items if item.get(key, 0) >= threshold]