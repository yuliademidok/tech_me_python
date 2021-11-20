from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .base_mixin import BaseMixin
from .meta import Base


class Tag(Base, BaseMixin):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), unique=True)

    @staticmethod
    def get_tag_authors(session, tag_name) -> list[object]:
        """все авторы, которые использовали указанный тег"""
        tag = session.query(Tag).filter(Tag.name == tag_name).first()
        tag_articles = tag.articles
        authors = [i.author for i in tag_articles]
        return list(set(authors))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
