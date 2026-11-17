import typing as t
from collections.abc import Iterable

def batch_process(data: Iterable[t.Any], batch_size: int = 10) -> t.Generator[list[t.Any], None, None]:
    """
    splits an iterable into smaller chunks for memory-efficient processing
    """
    if batch_size <= 0:
        raise ValueError("batch size must be positive")
    
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    
    if batch:
        yield batch

def clean_data_dict(data: dict[str, t.Any]) -> dict[str, t.Any]:
    """
    recursively removes keys with null values from a dictionary
    """
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, dict):
            value = clean_data_dict(value)
        
        if value is not None:
            cleaned[key] = value
            
    return cleaned

def flatten_list(nested_list: list[t.Any]) -> list[t.Any]:
    """
    flattens a nested list structure into a single dimension
    """
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat