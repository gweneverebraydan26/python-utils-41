import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_payload(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError(f"Invalid type: expected dict, got {type(data).__name__}")
    if not data:
        raise ValueError("Payload cannot be empty")
    return True

def process_items(items):
    """
    Main processing loop with input validation.
    Iterates through a list of items and performs validation.
    """
    for index, item in enumerate(items):
        try:
            validate_payload(item)
            logger.info(f"Processing item {index}: {item}")
            # Simulate core business logic
            result = item.get("value", 0) * 2
            print(f"Result: {result}")
        except (ValueError, TypeError) as e:
            logger.error(f"Validation failed at index {index}: {e}")
            continue

if __name__ == '__main__':
    data_batch = [{"value": 10}, {}, "invalid_string", {"value": 20}]
    process_items(data_batch)