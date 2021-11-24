import requests
from urllib.parse import urljoin, urlparse
import pathlib
import re

headers = {
    'User-Agent': "hey ho",
}

params = {
    "format[]": ["mm", "ms"],
    "category[]": "fruits_vegetables",
}


def get_page(url, to_save=False):
    response = requests.get(url)
    if to_save:
        temporary = url.split("/")
        file_path = pathlib.Path(__file__).parent.joinpath(f"{temporary[-1] or temporary[-2]}.html")
        with open(file_path, "wb") as f:
            f.write(response.content)
    return response





html_filepath = pathlib.Path(__file__).parent.joinpath("magnit_action.html")

# with open(html_filepath, "wb") as file:
#     file.write(response.content)

pattern = re.compile(r"href=\"(/promo\S+)\"")

url = 'https://magnit.ru/promo'
response = get_page(url)

products = set()
for link in re.findall(pattern, response.text):
    base = urlparse(response.url)
    url = urljoin(response.url, link)
    if base.netloc == urlparse(url).netloc:
        if url not in products:
            _ = get_page(url, to_save=True)
        products.add(url)

print(products)


print(1)
