import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
    ForeignKey,
    DateTime,
)

from habr_parse.database.meta import Base


_article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(64), unique=True)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String(255), unique=False)
    published_date = Column(DateTime, unique=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    author = relationship(Author, backref="articles")
    tags = relationship("Tag", secondary=_article_tag, backref="articles")

    @property
    def get_url(self):
        return self.url


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)


class PageErrors(Base):
    __tablename__ = "page_errors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_code = Column(String(3), unique=False)
    url = Column(String, unique=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
