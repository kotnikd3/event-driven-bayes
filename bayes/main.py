from bayes.application_services.services import IncrementalLearner
from bayes.infrastructure.connections import REDIS_CHANNEL, REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository
from bayes.infrastructure.subscribers import RedisSubscriber
from bayes.infrastructure.views import MatplotlibGraph

repository = RedisRepository(conn_string=REDIS_CONN_STRING)
repository.flush()

learner = IncrementalLearner(
    repository=repository,
    drawer=MatplotlibGraph,
)

redis_subscriber = RedisSubscriber(conn_string=REDIS_CONN_STRING)
redis_subscriber.subscribe(channel=REDIS_CHANNEL, learner=learner)
