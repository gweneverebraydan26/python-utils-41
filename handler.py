from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Handles incoming data payloads with configurable processors."""

    def __init__(self, default_strategy: Optional[Callable[[Any], Any]] = None) -> None:
        self._strategy = default_strategy or (lambda x: x)

    def process(self, data: Dict[str, Any], key: str) -> Any:
        """
        Extracts value by key and applies processing strategy.
        
        Args:
            data: Dictionary containing source information.
            key: Target key to retrieve.
            
        Returns:
            The processed value associated with the key.
        """
        raw_value = data.get(key)
        if raw_value is None:
            raise ValueError(f"Missing required key: {key}")
        return self._strategy(raw_value)

    def batch_process(self, items: list[Dict[str, Any]], key: str) -> list[Any]:
        """
        Processes a list of dictionaries for a specific key.
        
        Args:
            items: List of data dictionaries.
            key: Target key for each dictionary.
            
        Returns:
            List of processed values.
        """
        return [self.process(item, key) for item in items]