from flask import Flask

from api.application_services.publishers import Publisher
from api.domain import commands
from api.application_services import messagebus


class FlaskController:
    def __init__(self, publisher: Publisher):
        self.app = Flask(__name__)
        self.publisher = publisher

        @self.app.route("/", methods=['GET'])
        def api():
            return 'Api-publisher', 201

        @self.app.route("/update_model/<trial>", methods=['GET'])
        def update_model(trial):
            if trial in ('w', 'l'):
                command = commands.UpdateModel(trial)

                messagebus.handle(command, self.publisher)
                return 'Model updated', 201
            return 'Not found', 404


