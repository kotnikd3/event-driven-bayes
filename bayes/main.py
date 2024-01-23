import redis

from bayes.application_services.services import IncrementalLearner
from bayes.infrastructure.connections import REDIS_CONN_STRING
from bayes.infrastructure.repositories import RedisRepository
from bayes.infrastructure.views import MatplotlibGraph

engine = redis.from_url(REDIS_CONN_STRING)
repository = RedisRepository(engine=engine)
repository.flush()

learner = IncrementalLearner(repository=repository)

learner.update('w')
learner.update('l')
learner.update('w')
learner.update('w')
learner.update('w')
learner.update('l')
learner.update('w')
learner.update('l')
learner.update('w')

print(learner.model.predict())

graph = MatplotlibGraph(model=learner.model)
graph.draw()
graph.save('graphs')
