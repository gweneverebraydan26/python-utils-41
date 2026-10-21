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
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Ensure stream handler is present
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages to stdout."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = True) -> None:
        """Logs error messages including stack trace."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Logs warning level diagnostics."""
        self.logger.warning(message)

def get_default_logger() -> DataLogger:
    """Factory method for global logger instance."""
    return DataLogger()