from django.urls import path
from accounts.infrastructure.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register-api"),
]