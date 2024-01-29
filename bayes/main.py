# TODO move redis
import redis

from bayes.application_services.services import IncrementalLearner
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

redis_subscriber = RedisSubscriber(engine=engine)
# TODO move channel to the .env
redis_subscriber.subscribe(channel='update_model', learner=learner)
