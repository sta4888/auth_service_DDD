import pytest
from accounts.application.services import RegisterUserService
from accounts.domain.exceptions import DomainError

# Создаем фейковый (mock) репозиторий в памяти для теста,
# чтобы не тянуть Django ORM и базу данных на этапе юнит-теста.
class InMemoryUserRepository:
    def __init__(self):
        self.users = []

    def get_by_email(self, email):
        for user in self.users:
            if user.email.value == email.value:
                return user
        return None

    def save(self, user):
        self.users.append(user)


def test_register_user_success():
    """Проверяем успешную регистрацию нового пользователя через сервис."""
    repo = InMemoryUserRepository()
    service = RegisterUserService(user_repository=repo)

    # Вызываем сценарий использования
    user = service.execute(email="test@example.com", password="SecurePassword123")

    # Проверяем, что пользователь создан и сохранился в репозиторий
    assert user.email.value == "test@example.com"
    assert repo.get_by_email(user.email) == user


def test_register_user_already_exists():
    """Проверяем, что нельзя зарегистрировать двух пользователей с одинаковым email."""
    repo = InMemoryUserRepository()
    service = RegisterUserService(user_repository=repo)

    # Первая регистрация
    service.execute(email="test@example.com", password="SecurePassword123")

    # Вторая регистрация с тем же email должна вызвать доменную ошибку
    with pytest.raises(DomainError):
        service.execute(email="test@example.com", password="AnotherPassword123")