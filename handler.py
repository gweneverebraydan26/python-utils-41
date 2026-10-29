import logging
import os
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataHandler:
    """Manages data processing and lifecycle operations."""

    def __init__(self, storage_path: str = "./data"):
        self.storage_path = storage_path
        self._ensure_directory()

    def _ensure_directory(self) -> None:
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def process_payload(self, data: Dict[str, Any]) -> bool:
        """Validates and persists incoming dictionary payloads."""
        try:
            if not data or not isinstance(data, dict):
                raise ValueError("Invalid payload format")
            
            target = os.path.join(self.storage_path, "last_run.log")
            with open(target, "a", encoding="utf-8") as f:
                f.write(str(data) + "\n")
            
            logger.info(f"Successfully processed payload: {list(data.keys())}")
            return True
        except Exception as e:
            logger.error(f"Processing failure: {e}")
            return False

    def cleanup_old_logs(self, max_files: int = 5) -> None:
        """Prunes storage directory to keep footprint low."""
        files = [os.path.join(self.storage_path, f) for f in os.listdir(self.storage_path)]
        if len(files) > max_files:
            files.sort(key=os.path.getmtime)
            for f in files[:-max_files]:
                os.remove(f)
                logger.info(f"Cleaned up stale file: {f}")