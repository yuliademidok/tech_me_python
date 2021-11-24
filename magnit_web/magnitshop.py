import re

import requests
from urllib.parse import urljoin, urlparse
import pathlib
from abc import ABC, abstractmethod

from magnit_web.parser import Parser


class WebPage(ABC):

    @staticmethod
    @abstractmethod
    def get_page(url):
        pass


class MagnitShop(WebPage):

    MAIN_URL = 'https://magnit.ru'
    PROMO_URL = MAIN_URL + '/promo'
    promo_page_filepath = pathlib.Path(__file__).parent.joinpath("magnit_action.html")

    def __init__(self):
        pass

    @staticmethod
    def get_page(url, to_save=False, file_path=None):
        response = requests.get(url)
        if to_save:
            with open(file_path, "wb") as f:
                f.write(response.content)
        return response

    # def get_promo_page_response(self):
    #     return self.get_page(self.PROMO_URL, to_save=True, file_path=self.promo_page_filepath)

    # def get_promo_page_data(self) -> str:
    #     with open(self.promo_page_filepath, "rb") as f:
    #         promo_page_data = f.readlines()
    #     return str(promo_page_data)

    def _get_promo_data(self, pattern):
        data = set()
        promo_page = self.get_page(self.PROMO_URL)
        for datum in pattern.findall(promo_page.text):
            if datum not in data:
                data.add(datum)
                yield datum

    def get_promo_urls(self):
        for i in self._get_promo_data(Parser.promo_urls()):
            yield urljoin(self.PROMO_URL, i)

    def get_promo_title(self):
        return self._get_promo_data(Parser.promo_titles())

    # def get_promo_item_card(self):
    #     return self._get_promo_data(Parser.promo_item_card())

    def get_promo_urls_and_titles(self):
        urls_titles = []
        for i in self.get_promo_urls():
            url = Parser.promo_urls().findall(i)
            title = Parser.promo_titles().findall(i)
            if (url, title) not in urls_titles:
                urls_titles.append((url, title))
                yield (url, title)


if __name__ == '__main__':
    magnit = MagnitShop()

    # promo = magnit.get_promo_title()
    # promo = magnit.get_promo_urls()
    promo = magnit.get_promo_urls_and_titles()

    for i in promo:
        print(i)

