import requests
from urllib.parse import urljoin
import pathlib

from magnit_web import patterns


class WebPageMixin:

    @staticmethod
    def get_page(url, to_save=False, file_path=None):
        response = requests.get(url)
        if to_save:
            with open(file_path, "wb") as f:
                f.write(response.content)
        return response


class MagnitPage(WebPageMixin):

    main_url = 'https://magnit.ru'
    promo_url = main_url + '/promo'
    # promo_page_filepath = pathlib.Path(__file__).parent.joinpath("magnit_action.html")

    def __init__(self):
        pass

    def get_promo_main_page(self):
        return self.get_page(self.promo_url)

    def get_promo_urls(self):
        promo_page = self.get_promo_main_page().text
        for i in patterns.promo_urls().findall(promo_page):
            yield urljoin(self.promo_url, i)

    def _get_promo_item_page(self):
        for i in self.get_promo_urls():
            yield self.get_page(i)

    def get_promo_info(self):
        for i in self._get_promo_item_page():
            yield {"title": " ".join(patterns.promo_titles().findall(i.text)),
                   "url": i.url}
