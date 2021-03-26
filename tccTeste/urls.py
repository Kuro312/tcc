"""tccTeste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.forms import (
    ResetPasswordForm,
    NewPasswordForm,
)

from django.contrib.auth import (
    views,
)

urlpatterns = [
    path('', include('users.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),

    path('password_reset', views.PasswordResetView.as_view(
        template_name="users/pass_recover/reset_password.html", form_class=ResetPasswordForm), name='password_reset'),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(
        template_name="users/pass_recover/reset_password_done.html"), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name="users/pass_recover/reset_password_confirm.html", form_class=NewPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(
        template_name="users/pass_recover/reset_password_complete.html"), name="password_reset_complete"),
]
