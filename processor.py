import math
from typing import Any, Dict, List, Optional, Union


class ProcessingError(Exception):
    """Custom exception for unrecoverable processing failures."""
    pass


def safe_numeric_cast(value: Any, default: Optional[float] = None) -> Optional[float]:
    """Safely convert input to float, handling NaN, infinity, and type errors."""
    if value is None:
        return default
    try:
        val = float(value)
        if math.isnan(val) or math.isinf(val):
            return default
        return val
    except (ValueError, TypeError):
        return default


def process_batch(items: List[Any], key: Optional[str] = None) -> Dict[str, Union[int, float, List[Any]]]:
    """Process a list of items or dicts, handling invalid entries and edge cases cleanly."""
    if not isinstance(items, list):
        raise ProcessingError(f"Expected list for items, got {type(items).__name__}")

    sanitized = []
    numeric_vals = []
    skipped = 0

    for item in items:
        if item is None:
            skipped += 1
            continue

        target_val = item
        if key is not None:
            if not isinstance(item, dict) or key not in item:
                skipped += 1
                continue
            target_val = item[key]

        cast_val = safe_numeric_cast(target_val)
        if cast_val is not None:
            numeric_vals.append(cast_val)
            sanitized.append(item)
        else:
            skipped += 1

    total_valid = len(sanitized)
    avg_val = sum(numeric_vals) / total_valid if total_valid > 0 else 0.0

    return {
        "total_processed": len(items),
        "valid_count": total_valid,
        "skipped_count": skipped,
        "average": round(avg_val, 4),
        "sanitized_data": sanitized,
    }
