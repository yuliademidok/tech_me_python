import re


def promo_urls():
    return re.compile(r"href=\"(/promo\S+)/\"")


def promo_titles():
    return re.compile(r"class=\"action__title\">(.+?)</div>")
