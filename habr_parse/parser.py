import time
import typing
from datetime import datetime
from urllib.parse import urljoin

import requests
import bs4

from habr_parse.errors_handling import request_retry, soup_error_handling


class Parser:
    article_tag = None
    article_attr_tag_name = None
    article_attr_tag = None
    href_attr_tag = None
    article_title_tag = None
    article_title_attrs = None
    article_date_tag = None
    article_date_attrs_tag = None
    article_author_tag = None
    article_author_tag_attrs = None
    article_tag_tag = None
    article_tag_tag_attrs = None
    article_tag_tag_child = None
    article_tag_tag_attrs_child = None

    def __init__(self, database, start_url, delay=1.0):
        self.start_url = start_url
        self.done_urls = database.get_saved_urls()
        self.tasks = []
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))
        self.__parse_time = 0
        self.delay = delay
        self.database = database

    def get_task(self, url: str, callback: typing.Callable):
        def task():
            return callback(url)

        return task

    def run(self):

        while self.tasks:
            task = self.tasks.pop(0)
            data = task()
            if data:
                self.save_to_db(data)
            yield data

        self.get_next_page()

    def get_next_page(self):
        soup = self.get_soup(self.start_url)
        href = soup.find("a", attrs="tm-pagination__navigation-link").attrs.get("href")
        link = urljoin(self.start_url, href)
        self.start_url = link
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))

        result = self.run()
        for i in result:
            print(i)

        return self.start_url

    def save_to_db(self, page_data):
        self.database.save_parse_data(page_data)
        # pass

    @request_retry(count=2)
    def _get_response(self, url):
        next_time = self.__parse_time + self.delay
        now_time = time.time()
        if next_time > now_time:
            time.sleep(next_time - now_time)
        response = requests.get(url)
        self.__parse_time = now_time
        return response

    @soup_error_handling
    def get_soup(self, url):
        response = self._get_response(url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup

    def __links_parse(self, url, soup, value_name, callback):
        links = soup.find_all(self.article_tag, attrs={self.article_attr_tag: value_name})
        for itm in links:
            href = itm.attrs.get(self.href_attr_tag)
            if href:
                link = urljoin(url, href)
                if link not in self.done_urls:
                    self.tasks.append(self.get_task(link, callback))

    def rows_parse(self, url):
        soup = self.get_soup(url)
        if soup:
            self.__links_parse(url, soup, self.article_attr_tag_name, self.article_parse)

    def article_parse(self, url):
        soup = self.get_soup(url)
        title = soup.find(self.article_title_tag, attrs=self.article_title_attrs).text
        published_date = datetime.fromisoformat(soup.find(self.article_date_tag)
                                                .attrs.get(self.article_date_attrs_tag)[:-1])
        author = soup.find(self.article_author_tag, attrs=self.article_author_tag_attrs).text.strip()
        tags_children = soup.find(self.article_tag_tag, attrs=self.article_tag_tag_attrs). \
            find_all(self.article_tag_tag_child, attrs=self.article_tag_tag_attrs_child)
        tags = [tag.text for tag in tags_children]
        return {"url": url,
                "title": title,
                "published_date": published_date,
                "author": author,
                "tags": tags}
