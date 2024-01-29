from unittest import TestCase

import pytest

from api.infrastructure.repositories import RedisRepository


class TestRedisRepository(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, engine):
        self.engine = engine

    def test_pub_sub(self):
        repository = RedisRepository(self.engine)
        repository.flush()

        pub_sub = repository.pub_sub()
        pub_sub.publish('test', 'testing_message')
