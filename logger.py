import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "logs/app.log",
    level: int = logging.INFO,
    max_bytes: int = 10_485_760,
    backup_count: int = 5,
    console_output: bool = True,
) -> logging.Logger:
    """Configure and return a logger instance with rotating file handler support."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if already initialized
    if logger.hasHandlers():
        return logger

    log_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Configure rotating file handler if file path is provided
    if log_file:
        path = Path(log_file)
        if path.parent:
            path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    # Configure console standard output stream
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger
