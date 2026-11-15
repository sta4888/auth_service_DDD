import uuid
from accounts.domain.entities import User
from accounts.domain.value_objects import Email, Password
from accounts.domain.exceptions import UserAlreadyExistsError
from accounts.application.interfaces import AbstractUserRepository

class RegisterUserService:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> User:
        # 1. Создаем объекты-значения (тут происходит валидация формата)
        domain_email = Email(email)
        domain_password = Password(password)

        # 2. Проверяем бизнес-правило: существует ли уже такой пользователь
        existing_user = self.user_repository.get_by_email(domain_email)
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {email} already exists.")

        # 3. Создаем сущность
        new_user = User(
            id=uuid.uuid4(),
            email=domain_email,
            password=domain_password
        )

        # 4. Сохраняем через репозиторий
        self.user_repository.save(new_user)

        return new_user