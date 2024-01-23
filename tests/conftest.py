import pytest
import redis

from bayes.infrastructure.connections import REDIS_CONN_STRING


@pytest.fixture(scope='session')
def engine():
    yield redis.from_url(REDIS_CONN_STRING)
