"""Data validation utilities for batch processing loops."""

from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Raised when input data fails validation criteria."""
    pass


def validate_item(item: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate a single payload item before processing."""
    if not isinstance(item, dict):
        return False, "Input item must be a dictionary"

    if "id" not in item or not str(item["id"]).strip():
        return False, "Missing or empty 'id' field"

    if "name" not in item or not isinstance(item["name"], str):
        return False, "Missing or non-string 'name' field"

    if "value" in item and not isinstance(item["value"], (int, float)):
        return False, "Field 'value' must be numeric"

    return True, "OK"


def process_input_batch(items: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """Process a list of raw inputs, validating each item in the main loop."""
    processed = []
    errors = []

    for idx, raw_item in enumerate(items):
        is_valid, message = validate_item(raw_item)
        if not is_valid:
            errors.append({"index": idx, "item": raw_item, "error": message})
            continue

        # Standardize verified payload
        clean_item = {
            "id": str(raw_item["id"]).strip(),
            "name": raw_item["name"].strip(),
            "value": float(raw_item.get("value", 0.0)),
            "status": "validated",
        }
        processed.append(clean_item)

    return {"processed": processed, "errors": errors}
