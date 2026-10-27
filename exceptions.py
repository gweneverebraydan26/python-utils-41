"""Custom exceptions and error handling utilities for edge cases."""

import functools
import logging
from typing import Any, Callable, Optional, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


class BaseUtilError(Exception):
    """Base exception class for python-utils utility errors."""


class ValidationError(BaseUtilError):
    """Raised when input validation fails or data falls outside expected bounds."""

    def __init__(self, message: str, field_name: Optional[str] = None, value: Any = None):
        super().__init__(message)
        self.field_name = field_name
        self.value = value


class ProcessingError(BaseUtilError):
    """Raised when processing fails due to unhandled edge cases or state issues."""


def safe_execute(
    default_return: Any = None,
    catch_exceptions: tuple = (Exception,),
    log_errors: bool = True,
) -> Callable[[F], F]:
    """Decorator to safely execute functions and handle unexpected edge cases."""

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except catch_exceptions as err:
                if log_errors:
                    logger.warning("Edge case captured in %s: %s", func.__name__, err)
                return default_return

        return wrapper  # type: ignore

    return decorator


def ensure_non_null(value: Any, name: str = "value") -> Any:
    """Validate that a given value is not None or empty string."""
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValidationError(
            f"Parameter '{name}' cannot be null or empty", field_name=name, value=value
        )
    return value
