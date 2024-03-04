from .repositories import GenericRepository
from .rules import BusinessRule


class DomainException(Exception): ...


class BusinessRuleViolationException(DomainException):
    def __init__(self, rule: BusinessRule) -> None:
        self.rule = rule

    def __str__(self) -> str:
        return str(self.rule)


class EntityNotFoundException(Exception):
    def __init__(self, repository: GenericRepository, **kwargs) -> None:
        self.repository = repository
        self.kwargs = kwargs
        message = f"Entity with {kwargs} not found in {self.repository.__class__.__name__}"
        super().__init__(message)
