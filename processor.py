"""Data processing engine with input validation."""

from typing import Any, Dict, List


class InvalidInputError(Exception):
    """Raised when input item fails validation checks."""
    pass


class BatchProcessor:
    """Processes batches of data records with strict validation."""

    def __init__(self, required_keys: List[str]) -> None:
        self.required_keys = required_keys

    def validate_item(self, item: Any) -> Dict[str, Any]:
        """Validates a single record against expected structure and types."""
        if not isinstance(item, dict):
            raise InvalidInputError(f"Expected dict, got {type(item).__name__}")

        for key in self.required_keys:
            if key not in item:
                raise InvalidInputError(f"Missing required key: '{key}'")
            if item[key] is None:
                raise InvalidInputError(f"Value for '{key}' cannot be None")

        return item

    def process_batch(self, records: List[Any]) -> List[Dict[str, Any]]:
        """Main processing loop with input validation for incoming records."""
        processed_results: List[Dict[str, Any]] = []

        for index, raw_record in enumerate(records):
            try:
                valid_record = self.validate_item(raw_record)
                processed_item = {
                    "id": valid_record["id"],
                    "value": float(valid_record["value"]),
                    "status": str(valid_record.get("status", "pending")).lower(),
                }
                processed_results.append(processed_item)
            except (InvalidInputError, ValueError, TypeError) as err:
                print(f"Skipping invalid item at index {index}: {err}")

        return processed_results
