"""Custom exception classes for general data handling operations."""

from typing import Any, Dict, Optional


class BaseDataError(Exception):
    """Base exception class for all data utility errors."""

    def __init__(self, message: str, payload: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.payload = payload or {}

    def to_dict(self) -> Dict[str, Any]:
        """Return representation of the error as a dictionary."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "payload": self.payload,
        }

    def __str__(self) -> str:
        if self.payload:
            return f"{self.message} | Payload: {self.payload}"
        return self.message


class DataValidationError(BaseDataError):
    """Raised when data fails schema or condition validation checks."""

    def __init__(self, message: str, invalid_field: Optional[str] = None, value: Any = None):
        payload = {}
        if invalid_field is not None:
            payload["field"] = invalid_field
        if value is not None:
            payload["value"] = str(value)
        super().__init__(message, payload=payload)


class DataTransformationError(BaseDataError):
    """Raised when converting or transforming data structures fails."""

    def __init__(self, message: str, source_type: str, target_type: str):
        payload = {
            "source_type": source_type,
            "target_type": target_type,
        }
        super().__init__(message, payload=payload)


class DataNotFoundError(BaseDataError):
    """Raised when expected key or item is missing from data structure."""

    def __init__(self, message: str, key_path: Optional[str] = None):
        payload = {"key_path": key_path} if key_path else {}
        super().__init__(message, payload=payload)
