import pytest
import redis

from bayes.application_services.repositories import MemoryRepository
from bayes.application_services.services import AbstractGraph
from bayes.domain.models import StatisticalModel
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


class FakeGraph(AbstractGraph):
    def __init__(self, model: StatisticalModel):
        print('Initializing graph')
        super().__init__(model)

    def draw(self) -> None:
        print('Drawing graph')

    def save(self, name) -> None:
        print('Saving graph')


@pytest.fixture(scope='session')
def engine():
    yield redis.from_url(REDIS_CONN_STRING)
