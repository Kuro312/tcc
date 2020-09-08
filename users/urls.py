from django.contrib import admin
from django.urls import path
from users.views import (user_register,
                         user_login,
                         sair)

urlpatterns = [
    path('login', user_login, name='user_login'),
    path('register', user_register, name='user_register'),
    path('sair', sair, name='sair')
]
