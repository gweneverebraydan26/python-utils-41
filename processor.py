"""Data processing utilities for handling nested structures and record sets."""

from typing import Any, Dict, List, Optional


def flatten_dict(
    nested_dict: Dict[str, Any],
    parent_key: str = "",
    sep: str = ".",
) -> Dict[str, Any]:
    """Recursively flattens a nested dictionary using a character separator."""
    items: List[tuple] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                list_key = f"{new_key}{sep}{idx}"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, value))
    return dict(items)


def batch_process_records(
    records: List[Dict[str, Any]],
    flatten: bool = True,
    required_keys: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """Cleans, optionally flattens, and filters records based on key constraints."""
    processed_records = []
    for record in records:
        current = flatten_dict(record) if flatten else record.copy()
        # Verify all required keys exist in the record
        if required_keys and not all(k in current for k in required_keys):
            continue
        processed_records.append(current)
    return processed_records
