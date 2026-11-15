import pytest
from accounts.domain.value_objects import Email
from accounts.domain.exceptions import InvalidEmailError

def test_valid_email_creation():
    """Проверяем, что корректный email успешно создается."""
    email_str = "test@example.com"
    email = Email(email_str)
    assert email.value == email_str

def test_invalid_email_raises_error():
    """Проверяем, что некорректный email вызывает доменную ошибку."""
    with pytest.raises(InvalidEmailError):
        Email("not-an-email")