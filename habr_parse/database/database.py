from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from habr_parse.database.meta import Base
from habr_parse.database import models


class Database:

    def __init__(self, db_url):
        self.db_url = db_url
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def save_parse_data(self, data: dict):
        session = self.maker()
        author = models.Author(nickname=data["author"])
        article = models.Article(url=data["url"], title=data["title"], published_date=data["published_date"])
        author.articles.append(article)
        session.add(author)

        tags = [models.Tag(name=name) for name in data["tags"]]
        for tag in tags:
            tag.articles.append(article)
        session.add_all(tags)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
        finally:
            session.close()

    def save_errors(self, status_code, url):
        session = self.maker()
        error = models.PageErrors(status_code=status_code, url=url)
        session.add(error)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
        finally:
            session.close()

    def get_saved_urls(self):
        session = self.maker()
        urls = []
        for url in session.query(models.Article).all():
            urls.append(url.get_url)
        session.close()
        return urls
