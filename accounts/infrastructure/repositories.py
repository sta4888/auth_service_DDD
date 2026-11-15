from accounts.application.interfaces import AbstractUserRepository
from accounts.domain.entities import User
from accounts.domain.value_objects import Email, Password
from accounts.infrastructure.models import UserORM

class DjangoUserRepository(AbstractUserRepository):
    def get_by_email(self, email: Email) -> User | None:
        try:
            orm_user = UserORM.objects.get(email=email.value)
            return self._to_domain(orm_user)
        except UserORM.DoesNotExist:
            return None

    def save(self, user: User) -> None:
        # Создаем или обновляем запись в базе данных через Django ORM
        UserORM.objects.update_or_create(
            id=user.id,
            defaults={
                "email": user.email.value,
                "password": user.password.value,
            }
        )

    @staticmethod
    def _to_domain(orm_user: UserORM) -> User:
        """Маппер из ORM-модели в чистую доменную сущность."""
        return User(
            id=orm_user.id,
            email=Email(orm_user.email),
            password=Password(orm_user.password)
        )