import re
from datetime import datetime
from typing import Any, Dict, List

def validate_email(email: str) -> bool:
    """Check if the given string is a valid email address."""
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate international phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    cleaned = re.sub(r"[\s\-\(\)]", "", phone)
    pattern = r"^\+?\d{7,15}$"
    return bool(re.match(pattern, cleaned))

def validate_date(date_str: str, fmt: str = "%Y-%m-%d") -> bool:
    """Validate date string against specified format."""
    if not date_str or not isinstance(date_str, str):
        return False
    try:
        datetime.strptime(date_str, fmt)
        return True
    except (ValueError, TypeError):
        return False

def validate_password(password: str, min_length: int = 8) -> bool:
    """Validate password meets basic security requirements."""
    if not password or len(password) < min_length:
        return False
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
        return False
    return True

class ValidationResult:
    """Holds validation results for multiple checks."""
    def __init__(self):
        self.errors: List[str] = []
    def add_error(self, message: str) -> None:
        self.errors.append(message)
    def is_valid(self) -> bool:
        return len(self.errors) == 0
    def get_errors(self) -> List[str]:
        return self.errors.copy()

class DataValidator:
    """Reorganized validator for data dictionaries with chaining."""
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.result = ValidationResult()
    def check_email(self, field: str) -> "DataValidator":
        value = self.data.get(field)
        if value is not None and not validate_email(str(value)):
            self.result.add_error(f"Invalid email format for {field}")
        return self
    def check_phone(self, field: str) -> "DataValidator":
        value = self.data.get(field)
        if value is not None and not validate_phone(str(value)):
            self.result.add_error(f"Invalid phone format for {field}")
        return self
    def check_date(self, field: str, fmt: str = "%Y-%m-%d") -> "DataValidator":
        value = self.data.get(field)
        if value is not None and not validate_date(str(value), fmt):
            self.result.add_error(f"Invalid date format for {field}")
        return self
    def check_password(self, field: str, min_length: int = 8) -> "DataValidator":
        value = self.data.get(field)
        if value is not None and not validate_password(str(value), min_length):
            self.result.add_error(f"Weak password for {field}")
        return self
    def get_result(self) -> ValidationResult:
        return self.result