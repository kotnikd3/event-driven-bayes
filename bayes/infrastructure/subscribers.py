from typing import Callable

from bayes.infrastructure.repositories import RedisRepository


class RedisSubscriber:
    def __init__(self, repository: RedisRepository):
        self.repository = repository

    def subscribe(self, channel: str, handler: Callable):
        pubsub = self.repository.pub_sub(ignore_subscribe_messages=True)
        pubsub.subscribe(channel)

        print(f'Listening for messages on channel "{channel}".', flush=True)
        for event in pubsub.listen():
            handler(event)
