from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    List,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID

from bson import ObjectId
from mongoengine.base import BaseField
from mongoengine.document import Document, EmbeddedDocument
from typing_extensions import Literal

_T = TypeVar("_T")

_ST = TypeVar("_ST")
_GT = TypeVar("_GT")

class StringField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: StringField[Optional[str], Optional[str]],
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: StringField[Optional[str], str],
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[str, Callable[[], str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: StringField[str, str],
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[str, Callable[[], str], None] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: StringField[str, str],
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[str, Callable[[], str], None] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class EmailField(StringField[_ST, _GT]):
    @overload
    def __init__(
        self: EmailField[Optional[str], Optional[str]],
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: EmailField[Optional[str], str],
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[str, Callable[[], str]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: EmailField[str, str],
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[str, Callable[[], str], None] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: EmailField[str, str],
        domain_whitelist: Optional[List[str]] = ...,
        allow_utf8_user: bool = ...,
        allow_ip_domain: bool = ...,
        regex: Optional[str] = ...,
        max_length: Optional[int] = ...,
        min_length: Optional[int] = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[str, Callable[[], str], None] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[str]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class IntField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: IntField[Optional[int], Optional[int]],
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: IntField[Optional[int], int],
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[int, Callable[[], int]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: IntField[int, int],
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[int, Callable[[], int], None] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: IntField[int, int],
        min_value: int = ...,
        max_value: int = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[int, Callable[[], int], None] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[int]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class FloatField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: FloatField[Optional[float], Optional[float]],
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: FloatField[Optional[float], float],
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[float, Callable[[], float]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: FloatField[float, float],
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[float, Callable[[], float], None] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: FloatField[float, float],
        min_value: float = ...,
        max_value: float = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[float, Callable[[], float], None] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[float]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class DecimalField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: DecimalField[Optional[Decimal], Optional[Decimal]],
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DecimalField[Optional[Decimal], Decimal],
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[Decimal, Callable[[], Decimal]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DecimalField[Decimal, Decimal],
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[Decimal, Callable[[], Decimal], None] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DecimalField[Decimal, Decimal],
        min_value: Decimal = ...,
        max_value: Decimal = ...,
        force_string: bool = ...,
        precision: int = ...,
        rounding: str = ...,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[Decimal, Callable[[], Decimal], None] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[Decimal]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class BooleanField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: BooleanField[Optional[bool], Optional[bool]],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: bool = ...,
        choices: Optional[List[bool]] = ...,
        null: Literal[False] = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: BooleanField[Optional[bool], bool],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[bool, Callable[[], bool]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: BooleanField[bool, bool],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[bool, None, Callable[[], bool]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: BooleanField[bool, bool],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[bool, None, Callable[[], bool]] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[bool]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class DateTimeField(Generic[_ST, _GT], BaseField):
    @overload
    def __init__(
        self: DateTimeField[Optional[datetime], Optional[datetime]],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: None = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[datetime]] = ...,
        null: Literal[False] = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DateTimeField[Optional[datetime], datetime],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[False] = ...,
        default: Union[datetime, Callable[[], datetime]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DateTimeField[datetime, datetime],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: Literal[True] = ...,
        default: Union[datetime, None, Callable[[], datetime]] = ...,
        primary_key: Literal[False] = ...,
        choices: Optional[List[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DateTimeField[datetime, datetime],
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[datetime, None, Callable[[], datetime]] = ...,
        primary_key: Literal[True] = ...,
        choices: Optional[List[datetime]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: _ST) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _GT: ...

class EmbeddedDocumentField(Generic[_ST, _GT], BaseField):
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[False] = ...,
        default: None = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], Optional[_T]]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[False] = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], _T]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[True] = ...,
        default: None = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[_T, _T]: ...
    @overload
    def __new__(
        cls,
        document_type: Type[_T],
        required: Literal[True] = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T], _T]: ...
    def __set__(
        self: EmbeddedDocumentField[_ST, Any], instance: Any, value: _ST
    ) -> None: ...
    def __get__(
        self: EmbeddedDocumentField[Any, _GT], instance: Any, owner: Any
    ) -> _GT: ...

class DynamicField(BaseField): ...

class DictField(BaseField, Generic[_T]):
    # not sure we need the init method overloads
    @overload
    def __init__(
        self: DictField[StringField],
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[Dict[str, str], None, Callable[[], Dict[str, str]]] = ...,
        choices: Optional[List[Dict[str, str]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DictField[ListField[StringField]],
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[
            Dict[str, List[str]], None, Callable[[], Dict[str, List[str]]]
        ] = ...,
        choices: Optional[List[Dict[str, List[str]]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: DictField[_T],
        field: _T = ...,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[Dict[str, Any], None, Callable[[], Dict[str, Any]]] = ...,
        choices: Optional[List[Dict[str, Any]]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
    ) -> None: ...
    # TODO(sbdchd): use overloads to ensure we can only use nulls when
    # null=True is passed in
    @overload
    def __set__(
        self: DictField[StringField], instance: object, value: Optional[Dict[str, str]]
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[ListField[StringField]],
        instance: object,
        value: Optional[Dict[str, List[str]]],
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[_T], instance: object, value: Optional[Dict[str, _T]]
    ) -> None: ...
    @overload
    def __set__(
        self: DictField[Any], instance: object, value: Optional[Dict[str, Any]]
    ) -> None: ...
    @overload
    def __get__(
        self: DictField[DynamicField], instance: object, owner: object
    ) -> Dict[str, Any]: ...
    @overload
    def __get__(
        self: DictField[StringField], instance: object, owner: object
    ) -> Dict[str, str]: ...
    @overload
    def __get__(
        self: DictField[ListField[StringField]], instance: object, owner: object
    ) -> Dict[str, List[str]]: ...
    def __getitem__(self, arg: Any) -> _T: ...

class EmbeddedDocumentListField(BaseField, Generic[_T]):
    def __init__(
        self,
        kind: Type[_T],
        required: bool = ...,
        default: Optional[Any] = ...,
        help_text: str = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __set__(self, instance: Any, value: List[_T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> List[_T]: ...

class LazyReference(GenericField[Any, Any]):
    pass

class LazyReferenceField(GenericField[Any, Any]):
    def __init__(
        self,
        name: Union[str, Type[Document]],
        unique: bool = ...,
        required: bool = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...

class ListField(BaseField, Generic[_T]):
    # see: https://github.com/python/mypy/issues/4236#issuecomment-521628880
    @overload
    def __init__(
        self: ListField[StringField],
        field: _T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ListField[DictField[Any]],
        field: _T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ListField[_T],
        field: _T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    @overload
    def __set__(
        self: ListField[StringField], instance: Any, value: Optional[List[str]]
    ) -> None: ...
    @overload
    def __set__(
        self: ListField[DictField[Any]], instance: Any, value: List[Dict[str, Any]]
    ) -> None: ...
    @overload
    def __set__(self: ListField[_T], instance: Any, value: List[_T]) -> None: ...
    @overload
    def __get__(
        self: ListField[DynamicField], instance: Any, owner: Any
    ) -> List[Any]: ...
    @overload
    def __get__(
        self: ListField[StringField], instance: Any, owner: Any
    ) -> List[str]: ...
    @overload
    def __get__(
        self: ListField[DictField[Any]], instance: Any, owner: Any
    ) -> List[Dict[str, Any]]: ...

class UUIDField(GenericField[UUID, UUID]):
    def __init__(
        self,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[UUID, None, Callable[[], UUID]] = ...,
        choices: Optional[List[UUID]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
        binary: bool = ...,
    ) -> None: ...

class ObjectIdField(GenericField[ObjectId, ObjectId]):
    pass

class EmbeddedDocumentField(BaseField, Generic[_T]):
    @overload
    def __new__(
        cls,
        field: Type[_T],
        required: Literal[False] = ...,
        default: None = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[Optional[_T]]: ...
    @overload
    def __new__(
        cls,
        field: Type[_T],
        required: Literal[False] = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[_T]: ...
    @overload
    def __new__(
        cls,
        field: Type[_T],
        required: Literal[True] = ...,
        default: Union[_T, Callable[[], _T], None] = ...,
        help_text: str = ...,
    ) -> EmbeddedDocumentField[_T]: ...
    def __set__(self, instance: Any, value: Optional[_T]) -> None: ...
    @overload
    def __get__(self: EmbeddedDocumentField[_T], instance: Any, owner: Any) -> _T: ...
    @overload
    def __get__(
        self: EmbeddedDocumentField[Optional[_T]], instance: Any, owner: Any
    ) -> Optional[_T]: ...

_MapType = Dict[str, Any]

class MapField(DictField[_T]):
    pass
