

from httpx import Client, URL, QueryParams, Response
from typing import Any
from httpx._types import RequestData, RequestFiles

from httpx_client import client


class APIClient:
    def __init__(self,client: Client):
        self.client = client

    def get(self,url: URL | str, params : QueryParams | None = None) -> Response:
        return  self.client.get(url, params = params)

    def post(self,
             url: URL | str,
             json: Any | None = None,  # ПОЧЕМУ JSON ANY если он может принимать только JSON ? ТИПА DICT в Python.
             data: RequestData | None = None,
             files: RequestFiles | None = None)-> Response:
        return self.client.post(url, json= json, data = data,files = files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response: #ПОЧЕМУ МЫ ТУТ НЕ ПЕРЕДАЕМ ДРУГИЕ ФОРМАТЫ ДАННЫХ, КАК В ПОСТ, МЫ ЧТО, МОЖЕМ ОБНОВЛЯТЬ ДАННЫЕ С ТЕЛОМ ЗАПРОСА ТОЛЬКО В JSON ?  А ЕСЛИ МЫ СОЗДАЛИ РЕСУРС С ПОМОЩЬЮ DATA?
        return  self.client.patch(url, json= json)

    def delete(self,url: URL | str) -> Response:
        return self.client.delete(url)
