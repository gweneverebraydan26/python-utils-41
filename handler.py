from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Utility class for processing dictionaries with transformation logic."""

    def __init__(self, default_value: Any = None) -> None:
        """Initialize handler with a fallback default."""
        self.default_value = default_value

    def process(self, data: Dict[str, Any], key: str, transform: Optional[Callable[[Any], Any]] = None) -> Any:
        """Retrieve value from dictionary with optional transformation.

        Args:
            data: Input dictionary to query.
            key: The key to look up.
            transform: Optional function to apply to the value if found.

        Returns:
            Transformed value or default_value if missing.
        """
        if key not in data:
            return self.default_value

        value = data[key]
        return transform(value) if transform else value

    def batch_process(self, items: list[Dict[str, Any]], key: str) -> list[Any]:
        """Extract values for a specific key across a list of dictionaries."""
        return [item.get(key, self.default_value) for item in items]