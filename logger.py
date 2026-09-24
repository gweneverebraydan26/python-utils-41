import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logging utility for python-utils-41."""
    
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        """Configure console output formatting."""
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        self.logger.error(msg, exc_info=exc)

def get_logger(name: str) -> logging.Logger:
    """Factory function for consistent logger instances."""
    instance = AppLogger(name)
    return instance.logger