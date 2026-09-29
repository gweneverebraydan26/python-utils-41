import logging
import sys
from typing import Optional

class AppLogger:
    def __init__(self, name: str = 'python-utils-41', level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure console output format and handler."""
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_default_logger(name: Optional[str] = None) -> logging.Logger:
    """Factory function for standard application logging."""
    return AppLogger(name or 'python-utils-41').get_logger()