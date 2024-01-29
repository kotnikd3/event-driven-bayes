from abc import ABC, abstractmethod

from api.domain import commands


class Publisher(ABC):
    @abstractmethod
    def publish(self, command: commands.Command):
        raise NotImplementedError
