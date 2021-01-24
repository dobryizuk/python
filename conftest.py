import pytest
import datetime
import sys
sys.path.append('./framework')
import helper


@pytest.fixture(scope="function")
def schema():
    yield {
        "type": "object",
        "properties": {"userId": {"type": "number"},
                       "id": {"type": "number"},
                       "title": {"type": "string"},
                       "body": {"type": "string"}},
        "required": ["userId", "id", "title", "body"]
    }


@pytest.fixture(scope="function")
def content():
    yield {"userId": 4,
           "id": 31,
           "title": "ullam ut quidem id aut vel consequuntur",
           "body": "debitis eius sed quibusdam non quis consectetur vitae\nimpedit ut qui consequatur sed aut in\nquidem sit nostrum et maiores adipisci atque\nquaerat voluptatem adipisci repudiandae"
           }


@pytest.fixture(scope="function")
def response_delay():
    yield datetime.timedelta(seconds=0.5)


@pytest.fixture(scope="function")
def post_data():
    yield {"userId": 4,
           "id": 101,
           "title": "New test post pushisty hvost",
           "body": "Eleven benevolent elephants"
           }


@pytest.fixture(scope="function")
def post_wrong_data():
    yield {
        "id": "sdf",
        "userId": "sdfa",
        "title": "New test post pushisty hvost",
        "body": "Eleven benevolent elephants"
    }


@pytest.fixture(scope="function")
def random_data():
    yield {"userId": helper.random_int(),
           "id": helper.random_int(),
           "title": helper.random_word(),
           "body": helper.random_word()
           }
