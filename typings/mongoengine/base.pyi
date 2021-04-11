from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from bson import SON

U = TypeVar("U", bound="BaseDocument")

class BaseDocument:
    def to_mongo(self, use_db_field: bool = ..., fields: List[str] = ...) -> SON: ...
    def validate(self, clean: bool = ...) -> None: ...
    def to_json(self, *args: Any, **kwargs: Any) -> str: ...
    @classmethod
    def from_json(
        cls: Type[U], json_data: Dict[str, Any], created: bool = ...
    ) -> U: ...
    def _delta(self) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
    @classmethod
    def _get_collection_name(cls) -> Optional[str]: ...
    @classmethod
    def _from_son(
        cls: Type[U],
        son: Dict[str, Any],
        _auto_dereference: bool = ...,
        only_fields: Optional[List[str]] = ...,
        created: bool = ...,
    ) -> U: ...

_ST = TypeVar("_ST")
_GT = TypeVar("_GT")

class BaseField(Generic[_ST, _GT]):
    def __init__(
        self,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[_ST, None, Callable[[], _ST]] = ...,
        choices: Optional[List[_ST]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
        null: bool = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...
