from bayes.application_services import handlers
from bayes.application_services.services import IncrementalLearner
from bayes.domain import commands


def handle(command: commands.Command, learner: IncrementalLearner):
    for handler in HANDLERS[type(command)]:
        handler(command, learner)


HANDLERS = {
    commands.UpdateModel: [handlers.update_model],
}  # Dict[Type[commands.Command], List[Callable]]
