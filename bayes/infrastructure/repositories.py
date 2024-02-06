import redis

from bayes.application_services.repositories import MemoryRepository


class RedisRepository(MemoryRepository):
    def __init__(self, conn_string: str):
        self.engine = redis.from_url(conn_string, decode_responses=True)

    def flush(self):
        self.engine.flushdb()

    def save_data(self, data: dict) -> None:
        self.engine.hset('data', mapping=data)

    def get_data(self):
        return self.engine.hgetall('data')

    def pub_sub(self, **kwargs):
        return self.engine.pubsub(**kwargs)
