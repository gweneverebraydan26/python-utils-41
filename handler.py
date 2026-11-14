import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> bool:
    """Ensures payload is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False
    if 'id' not in data or 'payload' not in data:
        return False
    return True

def process_stream(data_stream: list) -> None:
    """Main loop for processing incoming data stream."""
    for index, entry in enumerate(data_stream):
        try:
            if not validate_payload(entry):
                logger.warning(f"Skipping invalid entry at index {index}")
                continue
            
            # Simulate core business logic
            item_id = entry['id']
            content = entry['payload']
            logger.info(f"Processing item {item_id}: {content}")
            
        except Exception as e:
            logger.error(f"Unexpected error at index {index}: {e}")

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'payload': 'data_a'},
        {'invalid': 'structure'},
        {'id': 2, 'payload': 'data_b'}
    ]
    process_stream(sample_data)