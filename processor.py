from typing import Any, Dict, List, Optional

def sanitize_data(data: Any, keys_to_strip: Optional[List[str]] = None) -> Any:
    """
    Recursively cleans input data by removing specified keys and normalizing strings.
    """
    if keys_to_strip is None:
        keys_to_strip = []

    if isinstance(data, dict):
        return {
            str(k): sanitize_data(v, keys_to_strip)
            for k, v in data.items()
            if k not in keys_to_strip
        }
    
    elif isinstance(data, list):
        return [sanitize_data(item, keys_to_strip) for item in data]
    
    elif isinstance(data, str):
        return data.strip()
    
    return data

def batch_process(items: List[Any], func: callable, batch_size: int = 10) -> List[Any]:
    """
    Executes a function across items in manageable chunks.
    """
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        try:
            results.extend([func(item) for item in batch])
        except Exception as e:
            print(f"Processing error at batch {i}: {e}")
            continue
    return results

def get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """
    Retrieves values from nested dictionary using dot notation.
    """
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default