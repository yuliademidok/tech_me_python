from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Table,
)

from .base_mixin import BaseMixin
from .meta import Base


_author_tag = Table(
    "author_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class Article(Base, BaseMixin):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(255), unique=False)
    data = Column(Text, unique=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", backref="articles")
    tags = relationship("Tag", secondary=_author_tag, backref="articles")

    def __str__(self):
        return self.subject

    def __repr__(self):
        return self.subject

