from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles transformation of dictionary-based datasets."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        self.settings: Dict[str, Any] = settings or {}

    def filter_keys(self, data: List[Dict[str, Any]], allowed: List[str]) -> List[Dict[str, Any]]:
        """
        Filters dictionaries to retain only specified keys.

        Args:
            data: List of dictionaries to process.
            allowed: List of keys to preserve.

        Returns:
            A filtered list of dictionaries.
        """
        return [{k: v for k, v in item.items() if k in allowed} for item in data]

    def flatten_values(self, data: List[Dict[str, Any]]) -> List[Any]:
        """
        Extracts all values from a list of dictionaries into a flat list.

        Args:
            data: List of dictionaries to flatten.

        Returns:
            A single list containing all values.
        """
        results: List[Any] = []
        for item in data:
            results.extend(item.values())
        return results

    def process_batch(self, data: List[Dict[str, Any]], key: str) -> List[Any]:
        """
        Extracts values for a specific key across the batch.

        Args:
            data: Input data list.
            key: Key to extract.

        Returns:
            List of values found for the given key.
        """
        return [item[key] for item in data if key in item]