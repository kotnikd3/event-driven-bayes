from api.application_services.publishers import Publisher
from api.domain import commands
from api.application_services import handlers


def handle(command: commands.Command, publisher: Publisher):
    for handler in HANDLERS[type(command)]:
        handler(command, publisher)


HANDLERS = {
    commands.UpdateModel: [handlers.publish_update_model],
}  # Dict[Type[commands.Command], List[Callable]]
