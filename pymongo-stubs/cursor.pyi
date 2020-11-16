from bson import SON
from pymongo.collation import Collation

class Cursor:
    def collation(self, collation: Collation) -> None: ...
    def _Cursor__query_spec(self) -> SON: ...

__all__ = ["Cursor"]
