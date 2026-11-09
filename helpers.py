import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict) -> bool:
    """Validates dictionary keys and value types."""
    required_fields = {'id': int, 'payload': str}
    
    if not isinstance(data, dict):
        return False
    
    for field, field_type in required_fields.items():
        if field not in data or not isinstance(data[field], field_type):
            return False
    return True

def process_main_loop(data_stream: list):
    """Processes data packets with integrated validation."""
    for entry in data_stream:
        if not validate_input_data(entry):
            logger.warning(f"Skipping invalid entry: {entry}")
            continue
        
        try:
            result = entry['id'] * 2
            print(f"Processed {entry['id']}: {result}")
        except Exception as e:
            logger.error(f"Critical processing failure: {e}")

if __name__ == "__main__":
    test_data = [{'id': 1, 'payload': 'data'}, {'id': 'error', 'payload': 'bad'}]
    process_main_loop(test_data)