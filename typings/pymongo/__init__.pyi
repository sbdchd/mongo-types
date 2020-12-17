from typing import Optional

import pymongo.cursor as cursor
from pymongo import change_stream, errors
from pymongo.cursor import Cursor
from pymongo.database import Database
from pymongo.operations import UpdateOne
from typing_extensions import Literal

ASCENDING: Literal[1] = 1
DESCENDING: Literal[-1] = -1
GEO2D: Literal["2d"] = "2d"
GEOHAYSTACK: Literal["geoHaystack"] = "geoHaystack"
GEOSPHERE: Literal["2dsphere"] = "2dsphere"
HASHED: Literal["hashed"] = "hashed"
TEXT: Literal["text"] = "text"

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
    def __getitem__(self, key: str) -> Database: ...
    def __getattr__(self, key: str) -> Database: ...
    def get_database(self) -> Database: ...
    def get_default_database(self) -> Database: ...
    admin: Database

class ReadPreference:
    NEAREST: object
    PRIMARY: object
    PRIMARY_PREFERRED: object
    SECONDARY: object
    SECONDARY_PREFERRED: object

__all__ = [
    "ASCENDING",
    "DESCENDING",
    "GEO2D",
    "GEOHAYSTACK",
    "GEOSPHERE",
    "HASHED",
    "TEXT",
    "Cursor",
    "MongoClient",
    "ReadPreference",
    "errors",
    "cursor",
    "UpdateOne",
    "change_stream",
]
