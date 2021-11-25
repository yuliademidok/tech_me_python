from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from magnit_web.database.meta import Base
from magnit_web.database.models import Magnit
from magnit_web.settings import DATABASES


class DB:

    def __init__(self):
        db_url = DATABASES['URL']
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


db = DB()
start_session = db.maker()
