from accounts.domain.exceptions import InvalidEmailError, WeakPasswordError

class Email:
    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    @staticmethod
    def _validate(value: str) -> None:
        if not value or "@" not in value or "." not in value.split("@")[-1]:
            raise InvalidEmailError(f"Invalid email format: {value}")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.value == other.value

    def __str__(self):
        return self.value


class Password:
    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    @staticmethod
    def _validate(value: str) -> None:
        if not value or len(value) < 8:
            raise WeakPasswordError("Password must be at least 8 characters long.")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other):
        if not isinstance(other, Password):
            return False
        return self.value == other.value

