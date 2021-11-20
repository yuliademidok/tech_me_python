from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .base_mixin import BaseMixin
from .meta import Base


class Author(Base, BaseMixin):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)

    @staticmethod
    def get_author_tags(session, author_name) -> list[object]:
        """все теги использованые указанным автором"""
        author = session.query(Author).filter(Author.name == author_name).first()
        author_articles = author.articles

        tags = list()
        for author in author_articles:
            tags.extend(list(author.tags))

        return list(set(tags))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
