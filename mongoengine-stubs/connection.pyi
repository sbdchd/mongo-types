from typing import Dict, Union

from pymongo import MongoClient

_connections: Dict[str, Union[MongoClient, object]]

__all__ = ["_connections"]
