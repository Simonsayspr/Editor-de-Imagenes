from abc import ABC, abstractmethod
from filters import Filter

class MenuItem(ABC):
    @classmethod
    @abstractmethod
    def get_description(cls) -> str:
        ...
    @classmethod
    @abstractmethod
    def ask_params(cls, im) -> str:
        ...
    @classmethod
    @abstractmethod
    def create_action(cls) -> Filter:
        ...