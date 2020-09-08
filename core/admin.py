from django.contrib import admin
from core.models import (
    Turma,
    Dia,
    Aluno,
)

# Register your models here.


admin.site.register(Turma)
admin.site.register(Dia)
admin.site.register(Aluno)
