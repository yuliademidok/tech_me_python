from habr_parse.parser import Parser
from habr_parse.database import database


class HabrParser(Parser):
    start_url = "https://habr.com/ru/all/"
    article_tag = "a"
    article_attr_tag_name = "tm-article-snippet__title-link"
    article_attr_tag = "class"
    href_attr_tag = "href"
    article_title_tag = "h1"
    article_title_attrs = {'class': 'tm-article-snippet__title'}
    article_date_tag = 'time'
    article_date_attrs_tag = 'datetime'
    article_author_tag = 'a'
    article_author_tag_attrs = {'class': "tm-user-info__username"}
    article_tag_tag = 'ul'
    article_tag_tag_attrs = {'class': "tm-separated-list__list"}
    article_tag_tag_child = 'li'
    article_tag_tag_attrs_child = {'class': "tm-separated-list__item"}

    def __init__(self, database, start_url=start_url, delay=1.0):
        super().__init__(database, start_url, delay)


if __name__ == '__main__':
    parser = HabrParser(database)

    result = parser.run()
    for i in result:
        print(i)
