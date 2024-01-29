from api.application_services.publishers import Publisher
from api.domain import commands
from api.infrastructure.repositories import RedisRepository


class RedisPublisher(Publisher):
    def __init__(self, repository: RedisRepository):
        self.repository = repository

    def publish(self, channel: str, command: commands.UpdateModel):
        print(
            f'Publishing message {str(command)} on channel "{channel}".',
            flush=True,
        )
        self.repository.pub_sub().publish(channel, command.trial)
