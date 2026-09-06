import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when a payload fails input validation rules."""
    pass


def validate_payload(payload: Dict[str, Any]) -> None:
    """Validate payload structure and field types before processing."""
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary")

    required_fields = ["task_id", "action", "data"]
    for field in required_fields:
        if field not in payload:
            raise ValidationError(f"Missing required field: '{field}'")

    if not isinstance(payload["task_id"], (str, int)):
        raise ValidationError("Field 'task_id' must be a string or integer")

    if not isinstance(payload["action"], str) or not payload["action"].strip():
        raise ValidationError("Field 'action' must be a non-empty string")

    if not isinstance(payload["data"], dict):
        raise ValidationError("Field 'data' must be a dictionary")


def process_task(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Execute processing logic for a valid task payload."""
    logger.info(f"Processing task {payload['task_id']}: {payload['action']}")
    return {"status": "success", "task_id": payload["task_id"]}


def run_processing_loop(items: List[Any]) -> List[Dict[str, Any]]:
    """Main processing loop with input validation for batch execution."""
    results = []
    for index, item in enumerate(items):
        try:
            validate_payload(item)
            result = process_task(item)
            results.append(result)
        except ValidationError as err:
            logger.warning(f"Validation failed for item at index {index}: {err}")
            results.append({"status": "rejected", "index": index, "error": str(err)})
        except Exception as err:
            logger.error(f"Unexpected error processing item at index {index}: {err}")
            results.append({"status": "error", "index": index, "error": "Internal failure"})

    return results
