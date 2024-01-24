# TODO: remove redis
import redis

from bayes.application_services import messagebus
from bayes.application_services.services import IncrementalLearner
from bayes.domain import commands
from bayes.infrastructure.connections import REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository
from bayes.infrastructure.views import MatplotlibGraph

engine = redis.from_url(REDIS_CONN_STRING)
repository = RedisRepository(engine=engine)
repository.flush()

learner = IncrementalLearner(
    repository=repository,
    drawer=MatplotlibGraph,
)

messagebus.handle(commands.UpdateModel('w'), learner)
messagebus.handle(commands.UpdateModel('l'), learner)
messagebus.handle(commands.UpdateModel('w'), learner)
messagebus.handle(commands.UpdateModel('w'), learner)
messagebus.handle(commands.UpdateModel('w'), learner)
messagebus.handle(commands.UpdateModel('l'), learner)
messagebus.handle(commands.UpdateModel('w'), learner)
messagebus.handle(commands.UpdateModel('l'), learner)
messagebus.handle(commands.UpdateModel('w'), learner)
