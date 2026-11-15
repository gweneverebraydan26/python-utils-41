import logging
import sys
from typing import Optional

class DataLogger:
    """Utility for standardized application logging."""
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Standard console handler
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_data(self, label: str, data: any) -> None:
        """Logs arbitrary data structures with a label."""
        try:
            self.logger.info(f"[{label}]: {repr(data)}")
        except Exception as e:
            self.logger.error(f"Logging failure for {label}: {e}")

    def capture_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Logs error context with optional exception details."""
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)

def get_logger(name: str = "python-utils-41") -> DataLogger:
    """Factory function for DataLogger instances."""
    return DataLogger(name)