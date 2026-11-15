import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from accounts.infrastructure.repositories import DjangoUserRepository
from accounts.application.services import RegisterUserService
from accounts.domain.exceptions import DomainError

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def get(self, request):
        email = request.GET.get("email")
        password = request.GET.get("password")
        return JsonResponse({"error": f"Invalid JSON {email} or server {password} error"}, status=400)


    def post(self, request, *args, **kwargs):
        try:
            # 1. Читаем JSON из тела запроса
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            # 2. Собираем зависимости (передаем наш Django репозиторий в сервис)
            repository = DjangoUserRepository()
            service = RegisterUserService(user_repository=repository)

            # 3. Выполняем сценарий использования
            user = service.execute(email=email, password=password)

            # 4. Возвращаем успешный ответ
            return JsonResponse(
                {"id": str(user.id), "email": user.email.value}, 
                status=201
            )

        except DomainError as e:
            # Если домен выбросил ошибку (слабый пароль, неверный email, дубликат) — возвращаем 400
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "Invalid JSON or server error"}, status=400)