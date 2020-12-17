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
from mongoengine.document import Document

T = TypeVar("T")

class GenericField(BaseField, Generic[T]):
    def __init__(
        self,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[T, None, Callable[[], T]] = ...,
        choices: Optional[List[T]] = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
        null: bool = ...,
    ) -> None: ...
    # TODO(sbdchd): use overloads to ensure we can only use nulls when
    # null=True is passed in
    def __set__(self, instance: Any, value: Optional[T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> T: ...

class IntField(GenericField[int]):
    def __init__(
        self,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[int, Callable[[], int], None] = ...,
        choices: Optional[List[int]] = ...,
        verbose_name: Optional[str] = ...,
        min: int = ...,
        max: int = ...,
        null: bool = ...,
    ) -> None: ...

class DecimalField(GenericField[Decimal]):
    pass

class EmailField(GenericField[str]):
    def validate(self, value: str) -> None: ...

class FloatField(GenericField[float]):
    pass

# @dataclass(frozen=True)
class StringField(GenericField[str]):
    def __init__(
        self,
        required: bool = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        help_text: Optional[str] = ...,
        default: Union[str, Callable[[], str]] = ...,
        choices: Optional[Sequence[str]] = ...,
        blank: bool = ...,
        verbose_name: Optional[str] = ...,
        db_field: str = ...,
        regex: str = ...,
        min_length: int = ...,
        max_length: int = ...,
        unique_with: str = ...,
        null: bool = ...,
    ) -> None: ...

# TODO(sbdchd): we can make this generic if we want better typing for assignment
#     workflow = fields.ReferenceField("Dialog")
# if we monkey patch we can make this generic like:
#     workflow = fields.ReferenceField[Dialog]("Dialog")

class ReferenceField(GenericField[Any]):
    def __init__(
        self,
        model: str,
        required: bool = ...,
        name: Optional[str] = ...,
        help_text: Optional[str] = ...,
        blank: bool = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> Any: ...

class BooleanField(GenericField[bool]):
    pass

class DateTimeField(GenericField[datetime]):
    pass

class DynamicField(GenericField[Any]):
    pass

class DictField(BaseField, Generic[T]):
    # not sure we need the init method overloads
    @overload
    def __init__(
        self: DictField[StringField],
        field: T = ...,
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
        field: T = ...,
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
        self: DictField[T],
        field: T = ...,
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
        self: DictField[T], instance: object, value: Optional[Dict[str, T]]
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
    def __getitem__(self, arg: Any) -> T: ...

class EmbeddedDocumentListField(BaseField, Generic[T]):
    def __init__(
        self, kind: Type[T], required: bool = ..., default: Optional[Any] = ...
    ) -> None: ...
    def __getitem__(self, arg: Any) -> T: ...
    def __iter__(self) -> Iterator[T]: ...
    def __set__(self, instance: Any, value: List[T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> List[T]: ...

class LazyReference(GenericField[Any]):
    pass

class LazyReferenceField(GenericField[Any]):
    def __init__(
        self,
        name: Union[str, Type[Document]],
        unique: bool = ...,
        required: bool = ...,
        help_text: Optional[str] = ...,
    ) -> None: ...

class ListField(BaseField, Generic[T]):
    # see: https://github.com/python/mypy/issues/4236#issuecomment-521628880
    @overload
    def __init__(
        self: ListField[StringField],
        field: T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ListField[DictField[Any]],
        field: T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ListField[T],
        field: T = ...,
        required: bool = ...,
        default: Optional[Union[List[Any], Callable[[], List[Any]]]] = ...,
        verbose_name: str = ...,
        help_text: str = ...,
        null: bool = ...,
    ) -> None: ...
    def __getitem__(self, arg: Any) -> T: ...
    def __iter__(self) -> Iterator[T]: ...
    @overload
    def __set__(
        self: ListField[StringField], instance: Any, value: Optional[List[str]]
    ) -> None: ...
    @overload
    def __set__(
        self: ListField[DictField[Any]], instance: Any, value: List[Dict[str, Any]]
    ) -> None: ...
    @overload
    def __set__(self: ListField[T], instance: Any, value: List[T]) -> None: ...
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

class UUIDField(GenericField[UUID]):
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

class ObjectIdField(GenericField[ObjectId]):
    pass

class EmbeddedDocumentField(BaseField, Generic[T]):
    def __init__(
        self,
        field: Type[T],
        required: bool = ...,
        default: Optional[Any] = ...,
        help_text: str = ...,
    ) -> None: ...
    def __set__(self, instance: Any, value: Optional[T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> T: ...

_MapType = Dict[str, Any]

class MapField(DictField[T]):
    pass
