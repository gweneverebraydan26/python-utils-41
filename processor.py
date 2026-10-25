import math
from typing import Any, Dict, List, Optional


class ProcessingError(Exception):
    """Custom exception raised when data processing encounters critical errors."""
    pass


class DataProcessor:
    """Utility class to process structured numerical and text data safely."""

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode

    def safe_numeric_cast(self, value: Any, default: float = 0.0) -> float:
        """Cast input value to float safely, handling NaN and Infinity edge cases."""
        if value is None:
            return default
        try:
            num = float(value)
            if math.isnan(num) or math.isinf(num):
                if self.strict_mode:
                    raise ProcessingError(f"Invalid numeric state encountered: {num}")
                return default
            return num
        except (ValueError, TypeError) as err:
            if self.strict_mode:
                raise ProcessingError(f"Failed to cast {value!r} to float: {err}") from err
            return default

    def process_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Process individual data records with edge case validation."""
        if not isinstance(record, dict):
            if self.strict_mode:
                raise ProcessingError(f"Expected dict record, got {type(record).__name__}")
            return {}

        cleaned_data: Dict[str, Any] = {}
        for key, val in record.items():
            if not isinstance(key, str) or not key.strip():
                continue  # Skip non-string or whitespace-only keys
            
            clean_key = key.strip().lower()
            if isinstance(val, (int, float, str)):
                cleaned_data[clean_key] = self.safe_numeric_cast(val)
            elif isinstance(val, list):
                cleaned_data[clean_key] = [self.safe_numeric_cast(item) for item in val]
            else:
                cleaned_data[clean_key] = None

        return cleaned_data

    def calculate_ratios(self, values: List[float], base: float) -> List[float]:
        """Compute ratios relative to base, safely avoiding division by zero."""
        safe_base = self.safe_numeric_cast(base, default=0.0)
        if safe_base == 0.0:
            return [0.0 for _ in values]

        results = []
        for item in values:
            safe_val = self.safe_numeric_cast(item, default=0.0)
            results.append(round(safe_val / safe_base, 4))
        return results
