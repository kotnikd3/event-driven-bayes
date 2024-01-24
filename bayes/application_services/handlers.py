from bayes.application_services.services import IncrementalLearner
from bayes.domain import commands


def update_model(command: commands.UpdateModel, learner: IncrementalLearner):
    learner.update(command.trial)
