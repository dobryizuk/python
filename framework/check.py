import allure
from hamcrest import assert_that, equal_to
from requests import codes
import jsonschema
import datetime


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _response_general_check_404(response, expected_code=codes.not_found):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _response_general_check_201(response, expected_code=codes.created):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_by_id_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(4))


@allure.step
def check_response_ok(response, length):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(length))


@allure.step
def check_create_new_post_response(response, length):
    _response_general_check_201(response)
    assert_that(len(response.json()), equal_to(length))


@allure.step
def check_get_post_by_wrong_id_response(response):
    _response_general_check_404(response)
    assert_that(len(response.json()), equal_to(0))


@allure.step
def check_get_post_response_content(response, response_testdata):
    json = response.json()
    assert_that(json[0]["id"] == response_testdata["id"])
    assert_that(json[0]["title"] == response_testdata["title"])
    assert_that(json[0]["userId"] == response_testdata["userId"])
    assert_that(json[0]["body"] == response_testdata["body"])


@allure.step
def check_new_post_response_content(response, post_data):
    json = response.json()
    assert_that(json["title"] == post_data["title"])
    assert_that(json["userId"] == post_data["userId"])
    assert_that(json["body"] == post_data["body"])


@allure.step
def check_change_post_response_content(response, post_data):
    json = response.json()
    assert_that(json["title"] == post_data["title"])
    assert_that(int(json["userId"]) == post_data["userId"])
    assert_that(json["body"] == post_data["body"])


@allure.step
def check_get_post_shema(response, schema):
    json = response.json()
    jsonschema.validate(instance=json, schema=schema)


@allure.step
def check_response_delay(response, delay):
    assert_that(delay > response.elapsed,
                f'Response delay is too long {response.elapsed}. Expected delay less {delay} ')
