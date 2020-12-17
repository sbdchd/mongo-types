from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from bson import SON
from pymongo.client_session import ClientSession
from pymongo.collation import Collation
from pymongo.collection import Collection

class CursorType:
    NON_TAILABLE: int
    TAILABLE: int
    TAILABLE_AWAIT: int
    EXHAUST: int

class Cursor:
    def __getitem__(self, index: int) -> Any: ...
    def add_options(self, mask: int) -> Cursor: ...
    @property
    def address(self) -> Optional[Tuple[str, int]]: ...
    @property
    def alive(self) -> bool: ...
    def allow_disk_use(self, allow_disk_use: bool) -> Cursor: ...
    def batch_size(self, batch_size: int) -> Cursor: ...
    def clone(self) -> Cursor: ...
    def close(self) -> None: ...
    def collation(self, collation: Collation) -> Cursor: ...
    @property
    def collection(self) -> Collection: ...
    def comment(self, comment: str) -> Cursor: ...
    def count(self, with_limit_and_skip: bool = ...) -> int: ...
    @property
    def cursor_id(self) -> Optional[int]: ...
    def distinct(self, key: str) -> List[Any]: ...
    def explain(self) -> Any: ...
    def hint(self, index: List[Tuple[str, Union[int, Dict[str, str]]]]) -> Cursor: ...
    def limit(self, limit: int) -> Cursor: ...
    def max(self, spec: List[Tuple[str, int]]) -> Cursor: ...
    def max_await_time_ms(self, max_await_time_ms: int) -> Cursor: ...
    def max_scan(self, max_scan: int) -> Cursor: ...
    def max_time_ms(self, max_time_ms: Optional[int]) -> Cursor: ...
    def min(self, spec: List[Tuple[str, int]]) -> Cursor: ...
    def next(self) -> Any: ...
    def remove_option(self, mask: int) -> Cursor: ...
    @property
    def retrieved(self) -> int: ...
    def rewind(self) -> Cursor: ...
    @property
    def session(self) -> Optional[ClientSession]: ...
    def skip(self, skip: int) -> Cursor: ...
    def sort(
        self,
        key_or_list: Union[str, List[Tuple[str, int]]],
        direction: Optional[int] = ...,
    ) -> Cursor: ...
    def where(self, where: str) -> Cursor: ...
    def _Cursor__query_spec(self) -> SON: ...
    def __iter__(self) -> Cursor: ...
    def __next__(self) -> Any: ...

class RawBatchCursor(Cursor): ...
