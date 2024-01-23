import pytest

from bayes.infrastructure.repositories import RedisRepository


@pytest.mark.usefixtures('engine')
class TestRedisRepository:
    def test_save_and_get_data(self, engine):
        repository = RedisRepository(engine)
        repository.save_data({'key': 11})

        assert {'key': 11}, repository.get_data()
