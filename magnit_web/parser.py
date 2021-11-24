import re


class Parser:

    @staticmethod
    def promo_urls():
        return re.compile(r"href=\"(/promo\S+)/\"")

    @staticmethod
    def promo_titles():
        return re.compile(r"<div class=\"card-sale__title\"><p>(.+?)</p></div>")

    @staticmethod
    def promo_item_card():
        return re.compile(r"href=\"(/promo[\S\n ]+)class=\"card-sale__footer")

    @staticmethod
    def promo_url_and_title():
        return re.compile(r"href=\"(/promo/\S+)\"|<div class=\"card-sale__title\"><p>(.+?)</p></div>")

