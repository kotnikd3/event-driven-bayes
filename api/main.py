from api.infrastructure.connections import REDIS_CONN_STRING
from api.infrastructure.controllers import FlaskController
from api.infrastructure.publishers import RedisPublisher

publisher = RedisPublisher(conn_string=REDIS_CONN_STRING)

controller = FlaskController(publisher=publisher)
server = controller.app
