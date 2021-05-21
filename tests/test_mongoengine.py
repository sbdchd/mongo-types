from __future__ import annotations

import datetime
import types
from enum import Enum
from typing import Any, KeysView, Type, TypeVar, Union, cast

import mongoengine
import pymongo
from bson import BSON, ObjectId
from mongoengine import Document, EmbeddedDocument, QuerySet, fields
from pymongo.collation import Collation, CollationStrength

mongoengine.connect("testdb")


T = TypeVar("T")


def no_op(self: T, x: object) -> T:
    return self


cast(Any, QuerySet).__class_getitem__ = types.MethodType(no_op, QuerySet)


class PostAttachment(EmbeddedDocument):
    url = fields.StringField()
    name = fields.StringField()


class PostQuerySet(QuerySet["Post"]):
    def for_org(self, *, org: str) -> QuerySet["Post"]:
        return self.filter(organization=org)

    def exists(self) -> bool:
        return self.count() > 0


class QuerySetManager:
    def __get__(self, instance: object, cls: Type[Post]) -> PostQuerySet:
        return PostQuerySet(cls, cls._get_collection())


class Recipe(Document):

    meta = {"collection": "recipes"}

    id = fields.ObjectIdField(primary_key=True, default=ObjectId)

    description = fields.StringField()


class Font(Enum):
    Helvetica = ("Helvetica",)
    Arial = ("Arial",)
    Times = "Times New Roman"


class Post(Document):
    meta = {
        "collection": "posts",
    }

    objects = QuerySetManager()

    @classmethod
    def dead_posts(cls) -> QuerySet[Post]:
        return cls.objects().filter(is_hidden=True)

    _id = fields.StringField(name="_id", primary_key=True)
    organization = fields.StringField(help_text="org where the post belongs")
    author = fields.StringField(required=False, help_text="Author of the post")
    title = fields.StringField()
    body = fields.StringField(help_text="contents of post")
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)
    kind = fields.StringField(choices=["new", "archive"])
    location = fields.StringField(required=False, default="home-page")
    is_hidden = fields.BooleanField(default=False)
    comment_count = fields.IntField(required=False)

    errors = fields.ListField(
        field=fields.DictField(field=fields.StringField()),
        default=[],
        help_text="some sort of errors",
    )
    results = fields.DictField()

    attachments = fields.EmbeddedDocumentListField(
        PostAttachment, required=False, help_text="random attachments"
    )
    main_attachment = fields.EmbeddedDocumentField(
        PostAttachment, required=True, help_text="random attachments"
    )
    tags = fields.MapField(
        required=False,
        field=fields.StringField(required=True),
        help_text=("Map tag names to descriptions"),
    )

    font = fields.EnumField(Font)
    font_required = fields.EnumField(Font, required=True)
    font_default = fields.EnumField(Font, default=Font.Helvetica)
    font_required_default = fields.EnumField(
        Font, required=True, default=Font.Helvetica
    )

    def set_hidden(self, hidden: bool) -> None:
        self.hidden = hidden
        self.save()

    def get_tag_names(self) -> KeysView[str]:
        return self.tags.keys()


PAGE_SIZE = 50


def main() -> None:
    author_id = "some-author-id"
    org_id = "some-org-id"
    offset = 10
    posts = list(
        Post.objects()
        .for_org(org=org_id)
        .filter(author=author_id, organization=org_id)
        .only(
            "_id",
            "title",
            "body",
            "created_at",
        )
        .order_by("-created_at")
        .skip(offset)
        # adding the extra 1 allows us to check if there are more pages to fetch
        .limit(PAGE_SIZE + 1)
    )
    print(posts)
    # reveal_type(posts)
    # Revealed type is 'builtins.list[test_mongoengine.Post*]

    posts_again = Post.objects().exclude("title").all_fields()
    print(posts_again)

    insert_result: list[Post] = Post.objects().insert([Post(), Post()])
    print(insert_result)

    insert_result_2: list[ObjectId] = Post.objects().insert(
        [Post(), Post()], load_bulk=False
    )
    print(insert_result_2)
    insert_result_3: Post = Post.objects().insert(Post())
    print(insert_result_3)
    insert_result_4: ObjectId = Post.objects().insert(Post(), load_bulk=False)
    print(insert_result_4)

    res: int = Post.objects().update(foo=True)
    print(res)

    name = "some_name"
    update_args = {f"foo_bar{name}_buzz": "buzz"}
    Post.objects().update(**update_args)
    Post.objects().update_one(**update_args)
    Post.objects().upsert_one(**update_args)

    first_post = posts[0]
    first_post.tags.values()
    first_post.errors
    first_post.results
    first_post.font

    def log_optional_font(f: Union[Font, None]) -> None:
        print(f)

    log_optional_font(first_post.font)

    def log_required_font(f: Font) -> None:
        print(f)

    log_required_font(first_post.font_required)
    first_post.font_required_default = None

    log_required_font(first_post.font_default)
    first_post.font_default = None

    p = Post()
    p.validate()
    p.save()

    assert Post.dead_posts().count() == 1

    assert Post.objects().none()
    assert Post.objects().get(id="foo")

    Post.objects().create(body="foo")
    Post.objects.create(body="foo")

    Post._get_collection().create_index(
        "name",
        name="name_unique_idx",
        unique=True,
        background=True,
        collation=Collation(
            locale="en", caseLevel=False, strength=CollationStrength.PRIMARY
        ),
    )
    Post._get_collection().create_index(
        [("foo", pymongo.ASCENDING), ("bar", pymongo.ASCENDING)],
        unique=True,
        partialFilterExpression={"_phone": {"$exists": True}},
    )

    assert len(Post.objects()) > 0
    assert len(Post.objects) > 0

    post = Post.objects().get()
    print(post._id)
    post.attachments[-1]
    list(post.attachments)
    print(post.main_attachment.name)

    x: Post = Post().save()
    print(x)

    recipe = Recipe().save()
    print(recipe.id)

    Post().reload()


def test_choices() -> None:
    roles = ("admin", "member", "viewer")
    roles_set = {"admin", "member", "viewer"}

    class Post:
        role = fields.StringField(choices=roles)
        role_set = fields.StringField(choices=roles_set)

    p = Post()
    assert p.role is None


def test_bson() -> None:
    doc = {"foo": "bar", "buzz": True}
    data = BSON.encode(doc)
    assert BSON.decode(data) == doc


def test_pymongo() -> None:
    pymongo.ALL
    pymongo.ASCENDING
    pymongo.CursorType
    pymongo.DESCENDING
    pymongo.DeleteMany
    pymongo.DeleteOne
    pymongo.GEO2D
    pymongo.GEOHAYSTACK
    pymongo.GEOSPHERE
    pymongo.HASHED
    pymongo.IndexModel
    pymongo.InsertOne
    pymongo.MAX_SUPPORTED_WIRE_VERSION
    pymongo.MIN_SUPPORTED_WIRE_VERSION
    pymongo.MongoClient
    pymongo.MongoReplicaSetClient
    pymongo.OFF
    pymongo.ReadPreference
    pymongo.ReplaceOne
    pymongo.ReturnDocument
    pymongo.SLOW_ONLY
    pymongo.TEXT
    pymongo.UpdateMany
    pymongo.UpdateOne
    pymongo.WriteConcern
    pymongo.aggregation
    pymongo.auth
    pymongo.auth_aws
    pymongo.bulk
    pymongo.change_stream
    pymongo.client_options
    pymongo.client_session
    pymongo.collation
    pymongo.collection
    pymongo.command_cursor
    pymongo.common
    pymongo.compression_support
    pymongo.cursor
    pymongo.cursor_manager
    pymongo.database
    pymongo.driver_info
    pymongo.encryption_options
    pymongo.errors
    pymongo.get_version_string
    pymongo.has_c
    pymongo.helpers
    pymongo.ismaster
    pymongo.max_staleness_selectors
    pymongo.message
    pymongo.mongo_client
    pymongo.mongo_replica_set_client
    pymongo.monitor
    pymongo.monitoring
    pymongo.monotonic
    pymongo.network
    pymongo.operations
    pymongo.periodic_executor
    pymongo.pool
    pymongo.read_concern
    pymongo.read_preferences
    pymongo.response
    pymongo.results
    pymongo.saslprep
    pymongo.server
    pymongo.server_description
    pymongo.server_selectors
    pymongo.server_type
    pymongo.settings
    pymongo.socket_checker
    pymongo.son_manipulator
    pymongo.srv_resolver
    pymongo.ssl_context
    pymongo.ssl_match_hostname
    pymongo.ssl_support
    pymongo.thread_util
    pymongo.topology
    pymongo.topology_description
    pymongo.uri_parser
    pymongo.version
    pymongo.version_tuple
    pymongo.write_concern

    def get_write_result() -> pymongo.results.BulkWriteResult:
        ...

    bulk_write_result = get_write_result()
    bulk_write_result.inserted_count
    bulk_write_result.matched_count

    try:
        print()
    except pymongo.errors.BulkWriteError as e:
        for error in e.details["writeErrors"]:
            assert "errmsg" in error and "op" in error
            print(error["errmsg"])
            phone = error["op"]["u"]["$set"]["_phone"]
            user_id = error["op"]["u"]["$set"]["_id"]
            print(phone)
            print(user_id)
