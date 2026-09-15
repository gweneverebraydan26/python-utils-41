import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when input item validation fails."""
    pass


class ItemHandler:
    """Handles validation and processing of batch input records."""

    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields

    def validate_item(self, item: Any) -> Dict[str, Any]:
        """Validate a single input record structure and contents."""
        if not isinstance(item, dict):
            raise ValidationError(f"Expected dict, got {type(item).__name__}")

        for field in self.required_fields:
            if field not in item or item[field] is None:
                raise ValidationError(f"Missing required field: '{field}'")

        if "id" in item and not isinstance(item["id"], (int, str)):
            raise ValidationError("Field 'id' must be an integer or string")

        return item

    def process_loop(
        self, raw_data: List[Any]
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Main processing loop with per-item input validation."""
        successful: List[Dict[str, Any]] = []
        failed: List[Dict[str, Any]] = []

        for index, raw_item in enumerate(raw_data):
            try:
                valid_item = self.validate_item(raw_item)
                # Perform processing on validated item
                valid_item["status"] = "processed"
                successful.append(valid_item)
            except ValidationError as err:
                logger.warning("Validation failed at index %d: %s", index, err)
                failed.append({"index": index, "raw": raw_item, "error": str(err)})

        return successful, failed
