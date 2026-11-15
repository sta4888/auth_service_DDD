# auth_service_DDD



```uv add django```

```uv add --dev pytest pytest-django ruff```

```
[tool.pytest.ini_options]

DJANGO_SETTINGS_MODULE = "config.settings"

python_files = ["test_*.py", "*_test.py"]

addopts = "--reuse-db"
```

```uv run django-admin startproject config .```

```uv run python manage.py startapp accounts```

# Создаем структуру слоев внутри accounts
```cmdmkdir -p accounts/domain accounts/application accounts/infrastructure accounts/tests/unit accounts/tests/integration```

```mkdir -p accounts/domain. accounts/application, accounts/infrastructure, accounts/tests/unit, accounts/tests/integration```


```shell
uv sync --all-extras --dev
```

```shell
uv run --frozen pytest
```