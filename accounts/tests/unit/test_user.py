import uuid
from accounts.domain.entities import User
from accounts.domain.value_objects import Email, Password

def test_user_creation():
    """Проверяем, что пользователь успешно создается с корректными данными."""
    user_id = uuid.uuid4()
    email = Email("test@example.com")
    password = Password("SecurePassword123")

    user = User(id=user_id, email=email, password=password)

    assert user.id == user_id
    assert user.email == email
    assert user.password == password

def test_users_equality_by_id():
    """Проверяем, что две сущности равны, если у них одинаковый ID (даже если другие поля отличаются)."""
    user_id = uuid.uuid4()
    email_1 = Email("test1@example.com")
    email_2 = Email("test2@example.com")
    password = Password("SecurePassword123")

    user1 = User(id=user_id, email=email_1, password=password)
    user2 = User(id=user_id, email=email_2, password=password)

    # В DDD сущности равны, если совпадает их ID
    assert user1 == user2