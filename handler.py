from typing import Any, Dict, List, Optional

class DataHandler:
    """Handles transformation and validation of data payloads."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        self.settings: Dict[str, Any] = settings or {}

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process a list of data dictionaries and return sanitized versions.
        
        Args:
            items: List of raw data dictionaries.
            
        Returns:
            List of processed data dictionaries.
        """
        results: List[Dict[str, Any]] = []
        for item in items:
            if self._is_valid(item):
                results.append(self._sanitize(item))
        return results

    def _is_valid(self, item: Dict[str, Any]) -> bool:
        """Verify that the item contains required schema keys."""
        return "id" in item and "payload" in item

    def _sanitize(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Remove sensitive fields from the data dictionary."""
        sanitized = item.copy()
        sanitized.pop("secret", None)
        return sanitized