from django.contrib import admin
from users.models import custom_user
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
# Register your models here.


class CustomAUserAdmin(UserAdmin):
    model = custom_user
    # fieldsets = [
    #     (None, {'fields': ('username', 'email',
    #                        'first_name', 'last_name', 'permissao', 'date_joined', 'telefone', 'is_staff', 'is_active', 'user_permissions'
    #                        )}),
    # ]
    # fields = ('username', 'email', 'first_name', 'last_name', 'permissao',
    #           'date_joined', 'telefone', 'is_staff', 'is_active', 'user_permissions')
    fieldsets = [
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'permissao',
                           'date_joined', 'telefone', 'is_staff', 'is_active', 'user_permissions')})]


admin.site.register(custom_user, CustomAUserAdmin)
