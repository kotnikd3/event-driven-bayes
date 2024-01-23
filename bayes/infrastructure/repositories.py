import redis

from bayes.application_services.repositories import MemoryRepository


class RedisRepository(MemoryRepository):
    def __init__(self, engine: redis.Redis):
        self.engine = engine

    def flush(self):
        self.engine.flushdb()

    def save_data(self, data: dict) -> None:
        self.engine.hset('data', mapping=data)

    def get_data(self):
        return self.engine.hgetall('data')
