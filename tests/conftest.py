import pytest
import redis

from bayes.application_services.repositories import MemoryRepository
from bayes.infrastructure.connections import REDIS_CONN_STRING


class FakeMemoryRepository(MemoryRepository):
    def __init__(self):
        self.engine = {}

    def flush(self):
        self.__init__()

    def save_data(self, data: dict) -> None:
        self.engine[b'data'] = data

    def get_data(self):
        if 'data' in self.engine:
            return self.engine[b'data']
        return None


@pytest.fixture(scope='session')
def engine():
    yield redis.from_url(REDIS_CONN_STRING)
