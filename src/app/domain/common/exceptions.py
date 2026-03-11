class NotFoundError(Exception):
    """Raised when a requested entity is not found."""


class ValidationError(Exception):
    """Raised when input data fails validation."""
