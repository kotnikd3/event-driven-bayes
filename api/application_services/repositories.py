from abc import ABC, abstractmethod


class MemoryRepository(ABC):
    @abstractmethod
    def pub_sub(self, **kwargs):
        raise NotImplementedError
