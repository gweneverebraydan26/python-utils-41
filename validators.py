import typing

def validate_numeric_input(value: typing.Any, min_val: float = 0, max_val: float = 100) -> float:
    """Ensures input is a valid number within range."""
    try:
        num = float(value)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Input {value} cannot be converted to float") from e
    
    if not (min_val <= num <= max_val):
        raise ValueError(f"Value {num} outside bounds [{min_val}, {max_val}]")
    
    return num

def validate_dict_keys(data: typing.Dict, required_keys: typing.List[str]) -> bool:
    """Checks for existence of keys in dictionary."""
    if not isinstance(data, dict):
        return False
    
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise KeyError(f"Missing required keys: {', '.join(missing)}")
    
    return True

def safe_list_access(items: typing.List, index: int, default: typing.Any = None) -> typing.Any:
    """Safely retrieves items from lists with index checking."""
    if not isinstance(items, list):
        return default
        
    try:
        return items[index]
    except IndexError:
        return default