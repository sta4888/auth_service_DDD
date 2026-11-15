import uuid
from accounts.domain.value_objects import Email, Password

class User:
    def __init__(self, id: uuid.UUID, email: Email, password: Password):
        self._id = id
        self._email = email
        self._password = password

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def email(self) -> Email:
        return self._email

    @property
    def password(self) -> Password:
        return self._password

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)