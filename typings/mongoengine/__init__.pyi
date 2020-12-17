from __future__ import annotations

from typing import Optional

from mongoengine.document import Document, DynamicDocument, EmbeddedDocument
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from mongoengine.queryset.queryset import QuerySet
from mongoengine.queryset.visitor import Q
from pymongo import MongoClient

def connect(name: str, alias: str = ..., host: Optional[str] = ...) -> MongoClient: ...
def register_connection(host: str, alias: str) -> None: ...

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
