import typing
from urllib.parse import urljoin

import requests
import bs4


class HabrParser:
    def __init__(self, start_url):
        self.start_url = start_url
        self.done_urls = set()
        self.tasks = []
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))

    def get_task(self, url: str, callback: typing.Callable):
        def task():
            return callback(url)

        return task

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            data = task()

    def get_soup(self, url):
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup

    def __links_parse(self, url, soup, class_name, callback):
        links = soup.find_all("a", attrs={"class": class_name})
        for i in links:
            href = i.attrs.get("href")
            if href:
                link = urljoin(url, href)
                self.tasks.append(self.get_task(link, self.rows_parse))

    def rows_parse(self, url):
        soup = self.get_soup(url)
        # pagination_links = soup.find_all("a", attrs={"class": "tm-pagination__page"})
        # for i in pagination_links:
        #     href = i.attrs.get("href")
        #     if href:
        #         link = urljoin(url, href)
        #         self.tasks.append(self.get_task(link, self.rows_parse))
        self.__links_parse(url, soup, "tm-pagination__page", self.rows_parse)
        self.__links_parse(url, soup, "tm-article-snippet__title-link", self.article_parse)

        # for i in soup.find_all("a", attrs={"class": "tm-article-snippet__title-link"}):
        #     pass

        print("1")

    def article_parse(self, url):
        soup = self.get_soup(url)
        title = self.__links_parse(url, soup, "tm-article-snippet__title tm-article-snippet__title_h1", self.article_parse)
        pass


if __name__ == '__main__':
    start_url = "https://habr.com/ru/all/"

    parser = HabrParser(start_url)
    parser.run()

    # response = requests.get(start_url)
    # soup = bs4.BeautifulSoup(response.text, "lxml")
    print(1)
