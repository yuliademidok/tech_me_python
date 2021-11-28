from functools import partial

from requests import HTTPError

from habr_parse.database import database


def request_retry(func=None, count=1):
    if func is None:
        return partial(request_retry, count=count)

    def wrapper(*args):
        nonlocal count
        while count:
            try:
                response = func(*args)
                response.raise_for_status()
                return func(*args)
            except HTTPError as exc:
                database.save_errors(exc.response.status_code, response.url)
                count -= 1
        return None

    return wrapper


def soup_error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            soup = func(*args, **kwargs)
            return soup
        except AttributeError:
            return None

    return wrapper
