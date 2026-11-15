# accounts/tests/unit/test_password.py

import pytest
from accounts.domain.value_objects import Password
from accounts.domain.exceptions import WeakPasswordError

def test_valid_password_creation():
    """Проверяем, что корректный пароль создается успешно."""
    pass_str = "SecurePassword123"
    password = Password(pass_str)
    assert password.value == pass_str

def test_too_short_password_raises_error():
    """Проверяем, что слишком короткий пароль вызывает ошибку."""
    with pytest.raises(WeakPasswordError):
        Password("short")