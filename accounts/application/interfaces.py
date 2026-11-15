from abc import ABC, abstractmethod
from accounts.domain.entities import User
from accounts.domain.value_objects import Email

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: Email) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass