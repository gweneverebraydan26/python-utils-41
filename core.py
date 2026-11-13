from typing import Any, Dict, List, Optional

class DataProcessor:
    """Handles transformation of dictionary data sets."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        self.settings: Dict[str, Any] = settings or {}

    def sanitize_keys(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Converts all dictionary keys to lowercase strings."""
        return {str(k).lower(): v for k, v in data.items()}

    def filter_by_prefix(self, data: Dict[str, Any], prefix: str) -> Dict[str, Any]:
        """Returns items where keys start with the provided prefix."""
        return {k: v for k, v in data.items() if k.startswith(prefix)}

    def batch_process(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Applies sanitization to a list of dictionaries."""
        return [self.sanitize_keys(item) for item in items]

def format_log_entry(message: str, level: str = "INFO") -> str:
    """Standardized formatter for system log messages."""
    return f"[{level.upper()}] {message.strip()}"

if __name__ == "__main__":
    processor = DataProcessor()
    sample = {"Name": "Test", "ID": 123}
    print(processor.sanitize_keys(sample))