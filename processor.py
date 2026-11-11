import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes incoming data items with strict schema validation."""

    REQUIRED_KEYS = {"id", "action", "payload"}
    VALID_ACTIONS = {"create", "update", "delete"}

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode

    def validate_item(self, item: Any) -> Tuple[bool, str]:
        """Validates a single input record for correct type and required fields."""
        if not isinstance(item, dict):
            return False, f"Expected dict, got {type(item).__name__}"

        missing_keys = self.REQUIRED_KEYS - set(item.keys())
        if missing_keys:
            return False, f"Missing required keys: {', '.join(sorted(missing_keys))}"

        if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
            return False, "Invalid 'id': must be non-empty string or integer"

        if item["action"] not in self.VALID_ACTIONS:
            return False, f"Invalid 'action': must be one of {sorted(self.VALID_ACTIONS)}"

        if not isinstance(item["payload"], dict):
            return False, "Invalid 'payload': must be a dictionary"

        return True, ""

    def process_batch(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Main processing loop with input validation for each entry."""
        successful = []
        failed = []

        for index, item in enumerate(items):
            is_valid, error_msg = self.validate_item(item)
            if not is_valid:
                logger.warning(f"Item at index {index} failed validation: {error_msg}")
                failed.append({"index": index, "item": item, "reason": error_msg})
                if self.strict_mode:
                    raise ValueError(f"Validation failed at index {index}: {error_msg}")
                continue

            item_id = item["id"]
            action = item["action"]
            payload_size = len(item["payload"])
            successful.append({"id": item_id, "action": action, "processed_fields": payload_size})

        return {
            "total": len(items),
            "successful_count": len(successful),
            "failed_count": len(failed),
            "successful": successful,
            "failed": failed,
        }
