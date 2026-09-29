import re
from typing import Any, Dict, Optional

def validate_payload(data: Dict[str, Any]) -> bool:
    """
    Validates core input structure for processing loop.
    Ensures required fields exist and match expected types.
    """
    required_fields = {'id': int, 'payload': str, 'timestamp': float}

    for field, field_type in required_fields.items():
        if field not in data:
            return False
        if not isinstance(data[field], field_type):
            return False

    # Validate payload format constraint
    if not re.match(r'^[a-zA-Z0-9_]{5,50}$', data['payload']):
        return False

    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitizes dictionary values by stripping whitespace from strings.
    """
    return {k: (v.strip() if isinstance(v, str) else v) for k, v in data.items()}

def process_safe(data: Any, handler_func: callable) -> Optional[Any]:
    """
    Orchestrates validation and sanitization before execution.
    """
    if not isinstance(data, dict):
        return None

    cleaned = sanitize_input(data)
    if not validate_payload(cleaned):
        return None

    return handler_func(cleaned)