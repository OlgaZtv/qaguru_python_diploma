import os

from api.helpers.requests_helper import BaseSession


def altoro() -> BaseSession:
    api_url = os.getenv('api_url')
    headers = {'content-type': 'application/json'}
    return BaseSession(base_url=api_url, headers=headers)
