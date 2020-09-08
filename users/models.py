from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class custom_user(AbstractUser):
    # 1 -> motorista
    # 2 -> aluno
    permissao = models.IntegerField(default=2)
    telefone = models.CharField(max_length=50,  default='1')
