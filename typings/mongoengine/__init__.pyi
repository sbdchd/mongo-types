from __future__ import annotations

from typing import Optional

from mongoengine.document import Document, DynamicDocument, EmbeddedDocument
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from mongoengine.queryset.queryset import QuerySet
from mongoengine.queryset.visitor import Q
from pymongo import MongoClient, ReadPreference

def connect(name: str, alias: str = ..., host: Optional[str] = ...) -> MongoClient: ...
def register_connection(alias: str, db: str = None, name: str = None, host: str = None, port: int = None, read_preference: ReadPreference = ReadPreference.Primary, username: str = None, password: str = None, authentication_source: str = None, authentication_mechanism: str = None, **kwargs) -> None: ...

__all__ = [
    "Q",
    "DoesNotExist",
    "QuerySet",
    "DynamicDocument",
    "EmbeddedDocument",
    "Document",
    "ValidationError",
    "NotUniqueError",
]
