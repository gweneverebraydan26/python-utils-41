import logging

logger = logging.getLogger(__name__)


def validate_input_item(item):
    """Validate that the input item is a non-empty dictionary with required keys."""
    if not isinstance(item, dict):
        raise TypeError(f"Expected dict, got {type(item).__name__}")
    
    if "id" not in item or "value" not in item:
        raise ValueError("Item is missing required keys: 'id' or 'value'")
    
    if not isinstance(item["id"], (int, str)):
        raise TypeError("Item 'id' must be an integer or string")

    return True


def process_items(input_data):
    """Main processing loop with input validation for python-utils-41."""
    results = []
    
    if not isinstance(input_data, list):
        logger.error("Processing failed: input must be a list")
        raise TypeError("Input data must be a list of items")

    for index, item in enumerate(input_data):
        try:
            validate_input_item(item)
            # Simulate processing valid item
            processed_value = item["value"]
            results.append({"id": item["id"], "processed": processed_value})
            logger.debug(f"Successfully processed item index {index}")
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping invalid item at index {index}: {e}")
            continue

    return results
