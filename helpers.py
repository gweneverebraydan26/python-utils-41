import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> Optional[Dict]:
    """Validate dictionary structure for processing loop."""
    if not isinstance(data, dict):
        logger.warning(f"Invalid input type: {type(data)}")
        return None
    
    required_keys = {'id', 'action', 'timestamp'}
    if not all(k in data for k in required_keys):
        logger.warning(f"Missing required keys in payload: {data.keys()}")
        return None

    return data

def process_main_loop(items: list):
    """Main loop with validation logic."""
    for item in items:
        validated = validate_payload(item)
        if validated is None:
            continue
        
        try:
            print(f"Processing ID: {validated['id']}")
        except Exception as e:
            logger.error(f"Execution error on item {item.get('id')}: {e}")