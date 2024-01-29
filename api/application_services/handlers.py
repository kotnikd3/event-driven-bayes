from api.application_services.publishers import Publisher
from api.domain import commands


def publish_update_model(command: commands.UpdateModel, publisher: Publisher):
    publisher.publish(command)
