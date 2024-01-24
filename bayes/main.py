# TODO move redis
import redis
from bayes.application_services import messagebus
from bayes.application_services.services import IncrementalLearner
from bayes.domain import commands
from bayes.infrastructure.connections import REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository
from bayes.infrastructure.subscribers import RedisSubscriber
from bayes.infrastructure.views import MatplotlibGraph

engine = redis.from_url(REDIS_CONN_STRING)
repository = RedisRepository(engine=engine)
repository.flush()

learner = IncrementalLearner(
    repository=repository,
    drawer=MatplotlibGraph,
)

# TODO move to handlers?
def handle(event):
    print(f'Handling: {event}', flush=True)

    trial = event['data'].decode('utf-8')

    command = commands.UpdateModel(trial)
    messagebus.handle(command, learner=learner)

redis_subscriber = RedisSubscriber(repository=repository)
# TODO move channel to the .env
redis_subscriber.subscribe('update_model', handle)
