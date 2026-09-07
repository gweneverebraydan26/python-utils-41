from typing import Dict, Any, Optional, Callable

class DataHandler:
    """Handles incoming data payloads for python-utils-41 processing."""

    def __init__(self, callback: Optional[Callable[[Any], None]] = None) -> None:
        self.callback = callback
        self.storage: Dict[str, Any] = {}

    def process_payload(self, key: str, value: Any) -> bool:
        """Stores data and triggers optional callback."""
        if not key or not isinstance(key, str):
            return False
        
        self.storage[key] = value
        if self.callback:
            self.callback(value)
        return True

    def get_data(self, key: str) -> Optional[Any]:
        """Retrieves value by key from internal storage."""
        return self.storage.get(key)

    def clear_storage(self) -> None:
        """Resets the current handler data storage."""
        self.storage.clear()

def example_callback(data: Any) -> None:
    """Example observer function for data changes."""
    print(f"Processing: {data}")

if __name__ == "__main__":
    handler = DataHandler(callback=example_callback)
    handler.process_payload("session_id", 1024)
    print(f"Value retrieved: {handler.get_data('session_id')}")