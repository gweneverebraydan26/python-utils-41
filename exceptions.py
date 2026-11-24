"""Custom exception hierarchy for application-wide error handling."""

from typing import Any, Dict, Optional


class BaseAppError(Exception):
    """Base exception class for all custom project errors."""

    def __init__(
        self,
        message: str,
        payload: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.payload = payload or {}
        self.code = code or "INTERNAL_ERROR"

    def to_dict(self) -> Dict[str, Any]:
        """Serialize exception details to a structured dictionary."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
            "payload": self.payload,
        }

    def __str__(self) -> str:
        if self.payload:
            return f"[{self.code}] {self.message} | Details: {self.payload}"
        return f"[{self.code}] {self.message}"


class ValidationError(BaseAppError):
    """Raised when input validation or schema checks fail."""

    def __init__(self, message: str, payload: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message, payload=payload, code="VALIDATION_ERROR")


class ConfigurationError(BaseAppError):
    """Raised when a required configuration setting is missing or invalid."""

    def __init__(self, message: str, payload: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message, payload=payload, code="CONFIG_ERROR")


class ProcessingError(BaseAppError):
    """Raised when data processing or pipeline execution fails."""

    def __init__(self, message: str, payload: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message, payload=payload, code="PROCESSING_ERROR")


class ResourceNotFoundError(BaseAppError):
    """Raised when a requested resource or key cannot be located."""

    def __init__(self, resource_id: str, resource_type: str = "Resource") -> None:
        message = f"{resource_type} '{resource_id}' was not found"
        payload = {"resource_id": resource_id, "resource_type": resource_type}
        super().__init__(message, payload=payload, code="NOT_FOUND")
