# urls.py in your application

from django.urls import path
from .views import ObtainTokenAPIView, UserRegistrationAPIView

urlpatterns = [
    # ... other url patterns ...
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", ObtainTokenAPIView.as_view(), name="login"),
]
