from typing import Optional

class ObjectId:
    def __init__(self, oid: Optional[str] = ...) -> None: ...
    @classmethod
    def is_valid(cls, oid: str) -> bool: ...
