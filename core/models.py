from django.db import models
from users.models import custom_user
# Create your models here.


class Turma(models.Model):
    motorista = models.ForeignKey(
        custom_user,  on_delete=models.DO_NOTHING)
    alunos = models.ManyToManyField(
        custom_user, related_name='%(class)s_alunos')
    vagas = models.IntegerField(default=10)
    vagas_restantes = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.motorista} - {self.vagas}'


class Dia(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False)
    turma = models.ForeignKey(
        Turma, on_delete=models.CASCADE, related_name='%(class)s_turmas')

    ativo = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return f'{self.data} - {self.turma}'


class Aluno(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE,
                            related_name='%(class)s_dias', null=False, blank=False, default=1)
    usuario = models.ForeignKey(
        custom_user,  on_delete=models.CASCADE)
    vai = models.BooleanField(default=True)
    volta = models.BooleanField(default=True)
    esta_na_ida = models.BooleanField(default=False)
    esta_na_volta = models.BooleanField(default=False)
