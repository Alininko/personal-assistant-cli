from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """Abstract base for all repositories. Implement per entity in infrastructure layer."""

    @abstractmethod
    def add(self, entity): ...

    @abstractmethod
    def get_by_id(self, entity_id: int): ...

    @abstractmethod
    def list_all(self): ...

    @abstractmethod
    def search(self, query: str): ...

    @abstractmethod
    def update(self, entity): ...

    @abstractmethod
    def delete(self, entity_id: int) -> None: ...
