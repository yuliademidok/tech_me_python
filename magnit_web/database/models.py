from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base


class Magnit(Base):
    __tablename__ = "promo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String, unique=False)

    def __str__(self):
        return self.url
