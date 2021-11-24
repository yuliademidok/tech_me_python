from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from .BaseMixin import BaseMixin
from .meta import Base


class Promo(Base, BaseMixin):
    __tablename__ = "promo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String, unique=False)
    # extract_date = Column(DateTime, unique=False)

    def __str__(self):
        return self.url
