from typing import Any

from pymongo import MongoClient, ReadPreference
from pymongo.database import Database

DEFAULT_CONNECTION_NAME: str
DEFAULT_DATABASE_NAME: str

class ConnectionFailure(Exception): ...

def register_connection(
    alias: str,
    db: str | None = ...,
    name: str | None = ...,
    host: str | None = ...,
    port: str | None = ...,
    read_preference: ReadPreference = ...,
    username: str | None = ...,
    password: str | None = ...,
    authentication_source: str | None = ...,
    authentication_mechanism: str | None = ...,
    **kwargs: Any,
) -> None: ...
def disconnect(alias: str | None = ...) -> None: ...
def disconnect_all() -> None: ...
def get_connection(
    alias: str | None = ...,
    reconnect: bool = ...,
) -> MongoClient: ...
def get_db(alias: str | None = ..., reconnect: bool = ...) -> Database: ...
def connect(
    db: str | None = ...,
    alias: str | None = ...,
    **kwargs: Any,
) -> MongoClient: ...

__all__ = [
    "DEFAULT_CONNECTION_NAME",
    "DEFAULT_DATABASE_NAME",
    "ConnectionFailure",
    "connect",
    "disconnect",
    "disconnect_all",
    "get_connection",
    "get_db",
    "register_connection",
]
