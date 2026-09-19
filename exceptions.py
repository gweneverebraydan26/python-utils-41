"""Custom exception hierarchy for general data handling utilities."""

from typing import Any, Optional


class BaseUtilError(Exception):
    """Base exception class for all utility package errors."""

    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details

    def __str__(self) -> str:
        if self.details is not None:
            return f"{self.message} (details: {self.details})"
        return self.message


class DataValidationError(BaseUtilError):
    """Raised when input data fails validation checks."""

    def __init__(self, message: str, field_name: Optional[str] = None, value: Any = None) -> None:
        details = {"field": field_name, "value": value} if field_name else None
        super().__init__(message, details=details)
        self.field_name = field_name
        self.value = value


class DataProcessingError(BaseUtilError):
    """Raised when an unexpected error occurs during data transformation."""

    pass


class ResourceNotFoundError(BaseUtilError):
    """Raised when a required data source or file cannot be located."""

    def __init__(self, resource_identifier: str, message: Optional[str] = None) -> None:
        msg = message or f"Resource not found: '{resource_identifier}'"
        super().__init__(msg, details={"resource": resource_identifier})
        self.resource_identifier = resource_identifier


class ConfigurationError(BaseUtilError):
    """Raised when utility configuration parameters are invalid or missing."""

    pass
