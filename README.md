# mongo-types [![PyPI](https://img.shields.io/pypi/v/mongo-types.svg)](https://pypi.org/project/mongo-types/)

Type stubs for [`mongoengine`][0] with some basic type stubs for [`pymongo`][1]
and [`bson`][2].

Allows for autocomplete and static typing.

## install

```shell
pip install mongo-types
```

Monkey patch mongoengine's `QuerySet` so we can type it with a generic
argument at runtime:

```python
import types
from mongoengine.queryset.queryset import QuerySet

def no_op(self, x):
    return self

QuerySet.__class_getitem__ = types.MethodType(no_op, QuerySet)
```

## usage

After installing and monkey patching, the types should work for the most
part,
but you'll probably need to change how you write some things.

### getting `objects` to work

By default, the base document is typed to not have an `objects` property so
that each document can type it properly.

Here's a helper class that's useful for simple cases which don't modify the
`QuerySet`.

```python
from typing import Generic, Type, TypeVar
from mongoengine import QuerySet, Document

U = TypeVar("U", bound=Document)

class QuerySetManager(Generic[U]):
    def __get__(self, instance: object, cls: Type[U]) -> QuerySet[U]:
        return QuerySet(cls, cls._get_collection())

class Page(Document):
    meta = {
        "collection": "pages",
    }

    objects = QuerySetManager["Page"]()

    organization = fields.StringField()
```

### replacing usages of `queryset_class`

before:

```python
from typing import Type
from mongoengine import QuerySet, Document

class PostQuerySet(QuerySet):
    def for_org(self, *, org: str) -> QuerySet:
        return self.filter(organization=org)

    def exists(self) -> bool:
        return self.count() > 0

class Post(Document):
    meta = {
        "collection": "posts",
        "queryset_class": SMSLogQuerySet,
    }

    organization = fields.StringField()
    # --snip--
```

after:

```python
from typing import Type
from mongoengine import QuerySet, Document

class PostQuerySet(QuerySet["Post"]):
    def for_org(self, *, org: str) -> QuerySet["Post"]:
        return self.filter(organization=org)

    def exists(self) -> bool:
        return self.count() > 0


class QuerySetManager:
    def __get__(self, instance: object, cls: Type[Post]) -> PostQuerySet:
        return PostQuerySet(cls, cls._get_collection())


class Post(Document):
    meta = {
        "collection": "posts",
    }

    objects = QuerySetManager()

    organization = fields.StringField()
    # --snip--
```

### replicating `@queryset_manager` behavior

before:

```python
from mongoengine import Document, QuerySet, queryset_manager, fields

class UserQuerySet(QuerySet):
    def for_org(self, *, org: str) -> QuerySet:
        return self.filter(organization=org)

class User(Document):
    meta = {
        "collection": "users",
        "queryset_class": UserQuerySet,
    }

    is_active = fields.BooleanField()

    # --snip--

    @queryset_manager
    def objects(self, queryset: QuerySet) -> QuerySet:
        return queryset.filter(is_active=True)

    @queryset_manager
    def all_objects(self, queryset: QuerySet) -> QuerySet:
        return queryset

maybe_user = User.all_objects.first()
```

after:

```python
from __future__ import annotations
from typing import Type
from mongoengine import QuerySet, Document

class UserQuerySet(QuerySet["User"]):
    def for_org(self, *, org: str) -> UserQuerySet:
        return self.filter(organization=org)


class QuerySetManager:
    def __get__(self, instance: object, cls: Type[User]) -> UserQuerySet:
        return UserQuerySet(cls, cls._get_collection()).filter(is_active=True)


class User(Document):
    meta = {
        "collection": "users",
    }

    is_active = fields.BooleanField()

    # --snip--

    objects = QuerySetManager()

    @classmethod
    def all_objects(cls) -> UserQuerySet:
        return UserQuerySet(cls, cls._get_collection())

maybe_user = User.all_objects().first()
```

### fixing "Model" has no attribute "id"

Mongoengine will define an `id` field for you automatically.
Mongo-types require you specify your `id` explicitly so that
the types can be more strict.

```python
class User(Document):
    meta = {
        "collection": "users",
    }

# becomes

class User(Document):
    meta = {
        "collection": "users",
    }
    id = fields.StringField(name="_id", primary_key=True, default=default_id)

# or if you prefer ObjectIds

class User(Document):
    meta = {
        "collection": "users",
    }
    id = fields.ObjectIdField(name="_id", primary_key=True, default=ObjectId)
```

## dev

```shell
poetry install

# run formatting, linting, and typechecking
s/lint

# build
poetry build -f wheel

# build and publish
poetry publish --build
```

[0]: https://github.com/MongoEngine/mongoengine
[1]: https://github.com/mongodb/mongo-python-driver/tree/master/pymongo
[2]: https://github.com/mongodb/mongo-python-driver/tree/master/bson
