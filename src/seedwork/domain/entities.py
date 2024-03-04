from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from .events import DomainEvent
from .mixins import BusinessRuleValidationMixin
from .value_objects import GenericId

EntityId = TypeVar("EntityId", bound=GenericId)


class Entity(BaseModel, Generic[EntityId]):
    id: EntityId = Field(hash=True)

    @classmethod
    def next_id(cls) -> EntityId:
        return cls.id.next_id()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id


class AggregateRoot(Entity[EntityId], BusinessRuleValidationMixin):
    events: list[DomainEvent] = []

    def register_event(self, event: DomainEvent) -> None:
        self.events.append(event)

    def collect_events(self) -> list[DomainEvent]:
        events = self.events
        self.events = []
        return events
