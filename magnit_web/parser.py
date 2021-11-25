from sqlalchemy.exc import IntegrityError

from magnit_web.magnit_page import MagnitPage
from magnit_web import database as db


class Parser:
    __products = []

    def __init__(self, ):
        page = MagnitPage()
        self.items = page.get_promo_info()
        self.session = db.start_session

    def save_to_db(self):
        for data in self.items:
            self.__products.append(db.Magnit(**data))

            if len(self.__products) > 4:
                try:
                    self.session.add_all(self.__products)
                    self.__products = []
                    self.session.commit()
                except IntegrityError:
                    self.session.rollback()
                finally:
                    self.session.close()
