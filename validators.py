import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input_data(data: Any) -> bool:
    """Validates dictionary structure for the processing loop."""
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dictionary")
        return False

    required_keys = {'id', 'payload', 'timestamp'}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - data.keys()
        logger.error(f"Missing required keys: {missing}")
        return False

    if not isinstance(data['id'], int):
        logger.error("Input validation error: 'id' must be an integer")
        return False

    return True

def process_main_loop(items: list[Any]) -> list[Any]:
    """Main loop with integrated input validation."""
    processed_results = []
    for item in items:
        if validate_input_data(item):
            try:
                # Core processing logic logic
                result = f"processed_{item['id']}"
                processed_results.append(result)
            except Exception as e:
                logger.warning(f"Processing failed for item {item.get('id')}: {e}")
        else:
            logger.debug("Skipping malformed input entry")
    
    return processed_results