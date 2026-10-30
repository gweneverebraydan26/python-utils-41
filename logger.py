import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logger configuration for python-utils-41."""
    
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure stdout handler with a consistent format."""
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        """Return the underlying configured logger instance."""
        return self.logger

def get_module_logger(name: str) -> logging.Logger:
    """Factory function for consistent module-level logging."""
    return AppLogger(name).get_logger()