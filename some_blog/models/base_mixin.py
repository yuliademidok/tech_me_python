from sqlalchemy.exc import IntegrityError


class BaseMixin:
    @classmethod
    def create(cls, session, **kwargs):
        obj = cls(**kwargs)
        try:
            session.add(obj)
            session.commit()
        except IntegrityError:
            session.rollback()
        return obj
