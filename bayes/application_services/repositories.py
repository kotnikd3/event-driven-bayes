from abc import ABC, abstractmethod


class MemoryRepository(ABC):
    @abstractmethod
    def save_data(self, data) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError
