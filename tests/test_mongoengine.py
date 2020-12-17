from __future__ import annotations

import datetime
import types
from typing import Any, KeysView, Type, TypeVar, cast

import mongoengine
import pymongo
from bson import ObjectId
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
        field=fields.DictField(field=fields.StringField()), default=[]
    )
    results = fields.DictField()

    attachments = fields.EmbeddedDocumentListField(PostAttachment, required=False)
    tags = fields.MapField(
        required=False,
        field=fields.StringField(required=True),
        help_text=("Map tag names to descriptions"),
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

    insert_result = Post.objects().insert([Post(), Post()])
    print(insert_result)

    insert_result_2 = Post.objects().insert([Post(), Post()], load_bulk=False)
    print(insert_result_2)

    first_post = posts[0]
    first_post.tags.values()
    first_post.errors
    first_post.results

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

    x: Post = Post().save()
    print(x)

    recipe = Recipe().save()
    print(recipe.id)

    Post().reload()
