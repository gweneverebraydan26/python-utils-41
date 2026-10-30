"""Data payload and event handler module for general utilities."""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")


class DataHandler:
    """Processes and transforms data payloads using registered pipelines."""

    def __init__(self, name: str = "default") -> None:
        """Initialize the data handler with a name and empty middleware pipeline.

        Args:
            name: Identifier for this handler instance.
        """
        self.name: str = name
        self._transformers: List[Callable[[Dict[str, Any]], Dict[str, Any]]] = []

    def register_transformer(
        self, func: Callable[[Dict[str, Any]], Dict[str, Any]]
    ) -> None:
        """Register a transformation function to be applied sequentially.

        Args:
            func: Function taking a payload dict and returning transformed dict.
        """
        self._transformers.append(func)

    def process_payload(
        self, payload: Dict[str, Any], fallback: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process a single payload dictionary through registered transformers.

        Args:
            payload: The incoming payload data.
            fallback: Optional dictionary to return if pipeline execution fails.

        Returns:
            Transformed dictionary payload or fallback value.
        """
        if not isinstance(payload, dict):
            return fallback if fallback is not None else {}

        result = payload.copy()
        try:
            for transformer in self._transformers:
                result = transformer(result)
            return result
        except Exception:
            return fallback if fallback is not None else {}

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process multiple dictionary payloads in sequence.

        Args:
            batch: List of input dictionaries to process.

        Returns:
            List of successfully processed dictionary payloads.
        """
        return [self.process_payload(item) for item in batch if isinstance(item, dict)]
