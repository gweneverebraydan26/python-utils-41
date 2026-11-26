"""Custom exception classes for general utility operations."""

from typing import Any, Optional


class UtilsBaseError(Exception):
    """Base exception for all python-utils errors."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            formatted_details = ", ".join(f"{k}={v!r}" for k, v in self.details.items())
            return f"{self.message} ({formatted_details})"
        return self.message


class ValidationError(UtilsBaseError):
    """Raised when data validation fails."""

    def __init__(self, message: str, field_name: Optional[str] = None, value: Any = None) -> None:
        details = {}
        if field_name is not None:
            details["field"] = field_name
        if value is not None:
            details["value"] = value
        super().__init__(message, details=details)


class ConfigurationError(UtilsBaseError):
    """Raised when configuration parameters are invalid or missing."""

    pass


class ProcessingError(UtilsBaseError):
    """Raised when generic data processing fails."""

    def __init__(self, message: str, original_cause: Optional[Exception] = None) -> None:
        details = {}
        if original_cause:
            details["cause"] = str(original_cause)
        super().__init__(message, details=details)
        self.original_cause = original_cause


class ResourceNotFoundError(UtilsBaseError):
    """Raised when a requested resource or file cannot be located."""

    pass
