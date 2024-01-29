import redis

from bayes.application_services import messagebus
from bayes.application_services.services import IncrementalLearner
from bayes.domain import commands


class RedisSubscriber:
    def __init__(self, conn_string: str):
        self.engine = redis.from_url(conn_string)

    def subscribe(self, channel: str, learner: IncrementalLearner):
        pubsub = self.engine.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(channel)

        print(f'Listening for messages on channel "{channel}".', flush=True)
        for message in pubsub.listen():
            self._handle_message(message, learner)

    @staticmethod
    def _handle_message(message, learner: IncrementalLearner):
        print(f'Handling: {message}', flush=True)

        trial = message['data'].decode('utf-8')

        command = commands.UpdateModel(trial)
        messagebus.handle(command, learner=learner)
