import os

from utils.api_requests_helper import BaseSession


def altoro() -> BaseSession:
    api_url = os.getenv('api_url')
    return BaseSession(base_url=api_url)
