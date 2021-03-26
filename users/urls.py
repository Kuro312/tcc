from django.contrib import admin
from django.urls import path
from users.views import (
    user_register,
    user_login,
    sair,
)
from django.contrib.auth import (
    views,
)

from users.forms import (
    ResetPasswordForm,
    NewPasswordForm,
)

app_name = "user"
urlpatterns = [
    path('', user_login, name='user_login'),
    path('register', user_register, name='user_register'),
    path('sair', sair, name='sair'),


]
