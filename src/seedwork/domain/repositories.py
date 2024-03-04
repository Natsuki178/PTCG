import abc
from typing import Generic, TypeVar

from .entities import Entity as DomainEntity
from .value_objects import GenericId

Entity = TypeVar("Entity", bound=DomainEntity)
EntityId = TypeVar("EntityId", bound=GenericId)


class GenericRepository(Generic[EntityId, Entity], metaclass=abc.ABCMeta):
    entity_id: EntityId

    @abc.abstractmethod
    def add(self, entity: Entity) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity: Entity) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, id: EntityId) -> Entity:
        raise NotImplementedError()

    @abc.abstractmethod
    def persist(self, entity: Entity) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def persist_all(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def collect_events(self) -> None:
        raise NotImplementedError()

    def __getitem__(self, index) -> Entity:
        return self.get_by_id(index)

    @classmethod
    def next_id(cls) -> EntityId:
        return cls.entity_id.next_id()
