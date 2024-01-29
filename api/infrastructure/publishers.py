import redis

from api.application_services.publishers import Publisher
from api.domain import commands
from api.infrastructure.connections import REDIS_CHANNEL


class RedisPublisher(Publisher):
    def __init__(self, conn_string: str):
        self.engine = redis.from_url(conn_string)

    def publish(self, command: commands.UpdateModel):
        print(
            f'Publishing message {str(command)} on channel "{REDIS_CHANNEL}".',
            flush=True,
        )
        self.engine.publish(REDIS_CHANNEL, command.trial)
