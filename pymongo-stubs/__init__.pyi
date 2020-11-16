from typing import Any, Dict, Optional, Sequence

import pymongo.cursor as cursor
from pymongo import errors
from pymongo.collation import Collation
from pymongo.cursor import Cursor

class UpdateOne:
    def __init__(self, *args: Dict[str, Any]) -> None: ...

class Collection:
    def create_index(
        self,
        field: str,
        name: str,
        unique: bool = ...,
        background: bool = ...,
        collation: Collation = ...,
    ) -> None: ...
    def bulk_write(self, updates: Sequence[UpdateOne]) -> Any: ...
    def update_many(
        self,
        match: Dict[str, Any],
        update: Dict[str, Any],
        array_filters: Sequence[Dict[str, Any]],
    ) -> Any: ...

class Database:
    name: str
    def command(self, command: Any) -> Any: ...
    def __getattr__(self, key: str) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...

class MongoClient:
    def __init__(
        self,
        host: Optional[str] = ...,
        port: int = ...,
        document_class: object = ...,
        tz_aware: Optional[object] = ...,
        connect: Optional[object] = ...,
        type_registry: Optional[object] = ...,
        **kwargs: object
    ) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __getattr__(self, key: str) -> Database: ...
    def get_database(self) -> Database: ...
    admin: Database

class ReadPreference:
    NEAREST: object
    PRIMARY: object
    PRIMARY_PREFERRED: object
    SECONDARY: object
    SECONDARY_PREFERRED: object

__all__ = [
    "Collection",
    "Cursor",
    "MongoClient",
    "ReadPreference",
    "errors",
    "cursor",
    "UpdateOne",
]
