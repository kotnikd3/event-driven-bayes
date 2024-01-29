import redis

from api.application_services.repositories import MemoryRepository


class RedisRepository(MemoryRepository):
    def __init__(self, engine: redis.Redis):
        self.engine = engine

    def pub_sub(self, **kwargs):
        return self.engine.pubsub(**kwargs)

    def flush(self):
        self.engine.flushdb()
