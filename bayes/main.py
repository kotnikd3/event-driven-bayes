import redis

from bayes.application_services.services import IncrementalLearner
from bayes.infrastructure.connections import REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository

engine = redis.from_url(REDIS_CONN_STRING)
repository = RedisRepository(engine=engine)
repository.flush()

learner = IncrementalLearner(repository=repository)

learner.update('W')
learner.update('L')
learner.update('W')
learner.update('W')
learner.update('W')
learner.update('L')
learner.update('W')
learner.update('L')
learner.update('W')

print(learner.model.predict())
