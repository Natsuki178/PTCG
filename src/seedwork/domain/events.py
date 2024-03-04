from pydantic import BaseModel


class DomainEvent(BaseModel):
    def __next__(self):
        yield self


class CompositeDomainEvent(BaseModel):
    events: list[DomainEvent]

    def __next__(self):
        yield from self
