from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from some_blog.models.meta import Base

from some_blog.models.author import Author
from some_blog.models.article import Article
from some_blog.models.tag import Tag
from some_blog.settings import DATABASES


class DB:

    def __init__(self):
        db_url = DATABASES['URL']
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


db_url = DATABASES['URL']
db = DB()
start_session = db.maker()
