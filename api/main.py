# TODO move redis
import redis

from api.infrastructure.connections import REDIS_CONN_STRING
from api.infrastructure.publishers import RedisPublisher
from api.infrastructure.repositories import RedisRepository
from api.infrastructure.controllers import FlaskController


engine = redis.from_url(REDIS_CONN_STRING)
repository = RedisRepository(engine=engine)
repository.flush()

publisher = RedisPublisher(repository=repository)

controller = FlaskController(publisher=publisher)
server = controller.app
