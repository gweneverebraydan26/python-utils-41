import json
import os
from typing import Any, Dict, Optional, Union

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Safely divide two numbers handling division by zero and invalid types."""
    try:
        if b == 0:
            return None
        return float(a) / float(b)
    except (TypeError, ValueError, ZeroDivisionError):
        return None

def safe_dict_get(data: Optional[Dict[str, Any]], key: str, default: Any = None) -> Any:
    """Retrieve value from dict with checks for None and missing keys."""
    if data is None or not isinstance(data, dict):
        return default
    try:
        return data.get(key, default)
    except Exception:
        return default

def safe_parse_int(value: Any, default: int = 0) -> int:
    """Convert value to int handling various edge cases."""
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return int(float(value))
        except (ValueError, TypeError):
            return default

def safe_read_file(filepath: str) -> str:
    """Read file content with error handling for common issues."""
    if not filepath or not isinstance(filepath, str):
        return ""
    if not os.path.exists(filepath):
        return ""
    if not os.access(filepath, os.R_OK):
        return ""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except (IOError, OSError, UnicodeDecodeError):
        return ""
    except Exception:
        return ""

def load_and_process_json(filepath: str) -> Dict[str, Any]:
    """Load JSON and process it safely handling edge cases."""
    content = safe_read_file(filepath)
    if not content:
        return {}
    try:
        data = json.loads(content)
        if not isinstance(data, dict):
            return {}
        processed = {}
        for k, v in data.items():
            if isinstance(k, str):
                processed[k] = safe_parse_int(v)
        return processed
    except json.JSONDecodeError:
        return {}
    except Exception:
        return {}