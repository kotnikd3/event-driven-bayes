import redis
from decouple import config

from bayes.application_services.repositories import MemoryRepository


class RedisRepository(MemoryRepository):

    def __init__(self):
        REDIS_HOST = config("REDIS_HOST")
        REDIS_PORT = config("REDIS_PORT")
        REDIS_DB = config("REDIS_DB")

        REDIS_CONN_STRING = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

        self.engine = redis.from_url(REDIS_CONN_STRING)

    def flush(self):
        self.engine.flushdb()

    def save_data(self, data: dict) -> None:
        self.engine.hset('data', mapping=data)

    def get_data(self):
        return self.engine.hgetall('data')
