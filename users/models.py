from django.db import models
from django.contrib.auth.models import AbstractUser
from mapbox_location_field.models import LocationField
# Create your models here.


class custom_user(AbstractUser):
    # 1 -> motorista
    # 2 -> aluno
    permissao = models.IntegerField(default=2)
    telefone = models.CharField(max_length=50,  default='1')
    local = LocationField(default=(0, 0), null=False)
