from bayes.application_services.services import IncrementalLearner
from bayes.infrastructure.repositories import RedisRepository

repository = RedisRepository()
repository.flush()

learner = IncrementalLearner(repository=repository)

learner.update("W")
learner.update("L")
learner.update("W")
learner.update("W")
learner.update("W")
learner.update("L")
learner.update("W")
learner.update("L")
learner.update("W")

print(learner.model.predict())
