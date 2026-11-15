import pytest
import uuid
from accounts.domain.entities import User
from accounts.domain.value_objects import Email, Password
from accounts.infrastructure.repositories import DjangoUserRepository


@pytest.mark.django_db
def test_django_user_repository_save_and_get():
    """Проверяем, что Django-репозиторий реально сохраняет пользователя в БД и достает его."""
    repo = DjangoUserRepository()

    user_id = uuid.uuid4()
    email = Email("db_test@example.com")
    password = Password("SecurePassword123")

    user = User(id=user_id, email=email, password=password)

    # Сохраняем через репозиторий
    repo.save(user)

    # Пытаемся найти пользователя в базе по email
    found_user = repo.get_by_email(email)

    assert found_user is not None
    assert found_user.id == user_id
    assert found_user.email.value == "db_test@example.com"
    assert found_user.password.value == "SecurePassword123"