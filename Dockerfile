# Используем официальный образ Python
FROM python:3.14-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем uv в системный путь
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Отключаем создание виртуального окружения uv (ставим всё в системный Python)
ENV UV_PROJECT_ENVIRONMENT="/usr/local"

# Копируем файлы конфигурации зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости в системный Python контейнера без создания .venv
RUN uv sync --frozen --no-dev --no-install-project --no-editable

# Копируем остальной код проекта
COPY . .

# Порт, на котором будет работать Django
EXPOSE 8000

# Так как зависимости уже в системе, можно запускать python напрямую (без uv run)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]