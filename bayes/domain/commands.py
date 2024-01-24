from abc import ABC
from dataclasses import dataclass


class Command(ABC):
    pass


@dataclass
class UpdateModel(Command):
    trial: str
