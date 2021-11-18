class DoesNotExist(Exception):
    pass

class FieldDoesNotExist(Exception):
    pass

class OperationError(Exception):
    pass

class NotUniqueError(OperationError):
    pass

class MultipleObjectsReturned(Exception):
    pass

class ValidationError(AssertionError):
    message: str

__all__ = [
    "DoesNotExist",
    "FieldDoesNotExist",
    "NotUniqueError",
    "OperationError",
    "ValidationError",
    "MultipleObjectsReturned",
]
