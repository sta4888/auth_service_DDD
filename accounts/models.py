from accounts.infrastructure.models import UserORM

# Экспортируем модель, чтобы Django ORM и миграции её видели
__all__ = ["UserORM"]