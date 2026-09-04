import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if "id" not in data or "payload" not in data:
        raise KeyError("Missing required keys: id, payload")
    return True

def process_items(items):
    """Main processing loop with integrated input validation."""
    results = []
    for item in items:
        try:
            if validate_input(item):
                logger.info(f"Processing item {item['id']}")
                # Simulated transformation logic
                processed = {"id": item["id"], "status": "success"}
                results.append(processed)
        except (ValueError, KeyError) as e:
            logger.error(f"Skipping invalid item: {e}")
            continue
        except Exception as e:
            logger.critical(f"Unexpected failure: {e}")
            break
    return results

if __name__ == "__main__":
    data_stream = [{"id": 1, "payload": "test"}, "invalid", {"id": 2, "payload": "data"}]
    process_items(data_stream)