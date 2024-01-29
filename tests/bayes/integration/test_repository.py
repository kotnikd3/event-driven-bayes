from unittest import TestCase

import pytest

from bayes.infrastructure.repositories import RedisRepository


class TestRedisRepository(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, engine):
        self.engine = engine

    def test_save_and_get_data(self):
        repository = RedisRepository(self.engine)
        repository.flush()
        repository.save_data({'key': b'11'})

        self.assertEqual({b'key': b'11'}, repository.get_data())
