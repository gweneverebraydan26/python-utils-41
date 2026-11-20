from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary structure into a single level.

    Args:
        data: The dictionary to flatten.
        parent_key: The string to prefix keys with.
        sep: The separator used for nested keys.

    Returns:
        A flattened dictionary with joined keys.
    """
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def format_byte_size(size: int, suffix: str = 'B') -> str:
    """
    Converts an integer byte size into a human-readable string.

    Args:
        size: The size in bytes.
        suffix: The unit suffix to append.

    Returns:
        A formatted string representation of the size.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(size) < 1024.0:
            return f"{size:3.1f}{unit}{suffix}"
        size /= 1024.0
    return f"{size:.1f}Yi{suffix}"