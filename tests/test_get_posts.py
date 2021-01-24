import allure
import pytest
import sys
sys.path.append('./framework')
sys.path.append('./')
from jsonplaceholder_client import Client
import conftest
import check


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):

        response = Client().get_all_posts()
        check.check_get_all_posts_response(response)

    @allure.title('Positive. Get by id')
    @pytest.mark.parametrize("id", [1, 2, 3])
    def test_get_posts_by_id(self, id, schema, response_delay):

        response = Client().get_post_by_id(id)
        check.check_get_post_by_id_response(response)
        check.check_get_post_shema(response, schema)
        check.check_response_delay(response, response_delay)

    @allure.title('Negative. Get by id')
    def test_get_posts_by_wrong_id(self, schema, response_delay):

        response = Client().get_post_by_id(333)
        check.check_get_post_by_wrong_id_response(response)
        check.check_response_delay(response, response_delay)

    @allure.title('Positive. Get by user_id')
    def test_get_posts_by_user_id(self, response_delay, content):

        response = Client().get_post_by_user_id(4)
        check.check_response_ok(response, 10)
        check.check_get_post_response_content(response, content)
        check.check_response_delay(response, response_delay)

    @allure.title('Negative. Get by user_id')
    def test_get_posts_by_wrong_user_id(self, response_delay):

        response = Client().get_post_by_user_id(222)
        check.check_response_ok(response, 0)
        check.check_response_delay(response, response_delay)


@allure.suite('POST')
class TestCreateNewPost:

    @allure.title('Positive. Post')
    def test_create_new_post(self, response_delay, post_data):

        response = Client().create_new_post(post_data)
        check.check_create_new_post_response(response, len(post_data))
        check.check_new_post_response_content(response, post_data)
        check.check_response_delay(response, response_delay)

    @allure.title('Negative. Post')
    def test_create_new_post(self, response_delay, post_wrong_data):

        response = Client().create_new_post(post_wrong_data)
        check.check_create_new_post_response(response, len(post_wrong_data))
        check.check_new_post_response_content(response, post_wrong_data)
        check.check_response_delay(response, response_delay)


@allure.suite('PUT')
class TestCreateNewPost:

    @allure.title('Positive. Put')
    def test_change_post(self, response_delay, random_data):
        response = Client().change_post(random_data, 1)
        check.check_response_ok(response, len(random_data))
        check.check_change_post_response_content(response, random_data)
        check.check_response_delay(response, response_delay)
