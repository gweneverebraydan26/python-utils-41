import logging
from typing import Any, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """Standard utility for processing iterative datasets."""

    def __init__(self, items: Optional[List[Any]] = None):
        self.items = items or []

    def clean(self) -> List[Any]:
        """Remove null entries from the dataset."""
        return [item for item in self.items if item is not None]

    def validate(self, predicate: Any) -> bool:
        """Ensure all items satisfy the provided condition."""
        if not self.items:
            return False
        return all(predicate(i) for i in self.items)

    def transform(self, func: Any) -> List[Any]:
        """Apply mapping function to internal list."""
        try:
            return [func(i) for i in self.items]
        except Exception as e:
            logger.error(f"Transformation failed: {e}")
            return []

    @staticmethod
    def create_batch(items: List[Any], size: int) -> List[List[Any]]:
        """Split data into chunks of fixed size."""
        return [items[i:i + size] for i in range(0, len(items), size)]