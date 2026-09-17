import re
from typing import Any, Optional

def validate_input(data: Any, expected_type: type, pattern: Optional[str] = None) -> bool:
    """Validates input type and optional regex pattern."""
    if not isinstance(data, expected_type):
        return False
    
    if pattern and isinstance(data, str):
        return bool(re.match(pattern, data))
    
    return True

def process_with_validation(data_list: list) -> list:
    """
    Main processing loop with input sanitization.
    Expects strings starting with 'ID-'.
    """
    validated_data = []
    pattern = r'^ID-\d{4,8}$'
    
    for item in data_list:
        # Validate type and format
        if validate_input(item, str, pattern):
            validated_data.append(item.strip())
        else:
            # Log invalid input (omitted for brevity)
            continue
            
    return validated_data

if __name__ == "__main__":
    raw_input = ["ID-1234", "INVALID", "ID-98765", 100]
    clean_data = process_with_validation(raw_input)
    print(f"Processed {len(clean_data)} valid items.")