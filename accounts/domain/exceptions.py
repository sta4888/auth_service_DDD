class DomainError(Exception):
    """Базовый класс для всех доменных ошибок."""
    pass


class InvalidEmailError(DomainError):
    """Выбрасывается, если передан некорректный формат email."""
    pass

class WeakPasswordError(DomainError):
    """Выбрасывается, если пароль не соответствует требованиям безопасности."""
    pass

class UserAlreadyExistsError(DomainError):
    """Выбрасывается, если пользователь с таким email уже существует."""
    pass