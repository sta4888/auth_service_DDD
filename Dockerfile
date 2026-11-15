# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем uv в системный путь
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Указываем uv использовать режим копирования вместо жестких ссылок (убирает предупреждение)
ENV UV_LINK_MODE=copy

# Копируем файлы конфигурации зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости проекта в системный python
RUN uv sync --frozen --no-dev --no-install-project --no-editable

# Копируем остальной код проекта
COPY . .

# Порт, на котором будет работать Django
EXPOSE 8000

# Запускаем сервер
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]