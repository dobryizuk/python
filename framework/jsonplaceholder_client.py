import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, json: dict, path: str):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=json)

    def _put(self, json: dict, path: str):
        return r.put(url=JSONPLACEHOLDER_HOST + path, data=json)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_post_by_user_id(self, user_id: int):
        return self._get(path=f'/posts/?userId={user_id}')

    @allure.step
    def create_new_post(self, json: dict):
        return self._post(json, path=f'/posts/')

    @allure.step
    def change_post(self, json: dict, post_id: int):
        return self._put(json, path=f'/posts/{post_id}')
