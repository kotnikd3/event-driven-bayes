from abc import ABC, abstractmethod
from typing import Callable


class Publisher(ABC):
    @abstractmethod
    def publish(self, channel: str, handler: Callable):
        raise NotImplementedError
