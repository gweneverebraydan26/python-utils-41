import logging
import sys
from typing import Optional

class DataLogger:
    """Utility class for standardized application logging."""

    def __init__(self, name: str = "python-utils-41", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Standard formatting for consistent log output
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        # Stream handler for stdout output
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)

def get_logger(name: str) -> DataLogger:
    """Factory function for global logger access."""
    return DataLogger(name)