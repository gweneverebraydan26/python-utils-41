from typing import List, Any, Optional, Dict
import datetime

def format_data(items: List[Dict[str, Any]], key: str) -> List[Any]:
    """Extract values from list of dicts based on key.

    Args:
        items: List of dictionaries to parse.
        key: The dictionary key to extract.

    Returns:
        A list of values associated with the specified key.
    """
    return [item[key] for item in items if key in item]

def generate_timestamp() -> str:
    """Create a string representation of current UTC time.

    Returns:
        ISO format string of the current UTC timestamp.
    """
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def filter_none(data: Dict[str, Optional[Any]]) -> Dict[str, Any]:
    """Remove keys with None values from a dictionary.

    Args:
        data: Input dictionary to filter.

    Returns:
        A new dictionary excluding None values.
    """
    return {k: v for k, v in data.items() if v is not None}

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller sub-lists of a defined size.

    Args:
        items: The list to be divided.
        size: The maximum size of each chunk.

    Returns:
        A list of list chunks.
    """
    return [items[i:i + size] for i in range(0, len(items), size)]