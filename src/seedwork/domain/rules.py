from pydantic import BaseModel


class BusinessRule(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    __message: str = "Business Rule Violation"

    def is_broken(self) -> bool:
        raise NotImplementedError

    @property
    def message(self) -> str:
        return self.__message

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {super().__str__()}"
