from unittest import TestCase

from bayes.infrastructure.connections import REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository


class TestRedisRepository(TestCase):
    def test_save_and_get_data(self):
        repository = RedisRepository(REDIS_CONN_STRING)
        repository.flush()

        repository.save_data({'key': '11'})
        self.assertEqual({'key': '11'}, repository.get_data())
