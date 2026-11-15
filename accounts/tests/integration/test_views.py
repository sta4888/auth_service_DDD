import pytest
from django.urls import reverse
from accounts.infrastructure.models import UserORM


@pytest.mark.django_db
def test_register_api_success(client):
    """Проверяем, что эндпоинт регистрации успешно создает пользователя через HTTP-запрос."""
    url = reverse("register-api")  # Имя нашего будущего эндпоинта
    data = {
        "email": "api_test@example.com",
        "password": "SecurePassword123"
    }

    response = client.post(url, data, content_type="application/json")

    assert response.status_code == 201
    response_data = response.json()
    assert response_data["email"] == "api_test@example.com"

    # Проверяем, что пользователь реально появился в базе
    assert UserORM.objects.filter(email="api_test@example.com").exists()


@pytest.mark.django_db
def test_register_api_weak_password(client):
    """Проверяем, что при слабом пароле возвращается ошибка валидации."""
    url = reverse("register-api")
    data = {
        "email": "api_test@example.com",
        "password": "short"  # Слишком короткий пароль
    }

    response = client.post(url, data, content_type="application/json")

    assert response.status_code == 400
    assert "error" in response.json()