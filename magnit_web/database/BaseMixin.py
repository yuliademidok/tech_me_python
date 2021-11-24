from typing import Iterable

from sqlalchemy.exc import IntegrityError


class BaseMixin:
    @classmethod
    def create_one(cls, session, **kwargs) -> object:
        obj = cls(**kwargs)
        try:
            session.add(obj)
            session.commit()
        except IntegrityError:
            session.rollback()
        return obj

    # @staticmethod
    # def create_all(session, **kwargs):
    #     objs = [i for i in kwargs]
    #     try:
    #         session.add_all(objs)
    #         session.commit()
    #     except IntegrityError:
    #         session.rollback()
    #     return objs
