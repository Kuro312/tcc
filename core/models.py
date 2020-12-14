from django.db import models
from users.models import custom_user
from mapbox_location_field.models import LocationField
# Create your models here.


class Turma(models.Model):
    motorista = models.ForeignKey(
        custom_user,  on_delete=models.DO_NOTHING)
    alunos = models.ManyToManyField(
        custom_user, related_name='%(class)s_alunos')
    nome = models.CharField(max_length=100, default="")

    local = LocationField(default=(0, 0), null=False, map_attrs={
        "style": "mapbox://styles/mapbox/outdoors-v11",
        "zoom": 13,
        "center": [17.031645, 51.106715],
        "cursor_style": 'pointer',
        "marker_color": "red",
        "rotate": False,
        "geocoder": True,
        "fullscreen_button": True,
        "navigation_buttons": True,
        "track_location_button": True,
        "readonly": True,
        "placeholder": "Pick a location on map below", })

    def __str__(self):
        return f'{self.motorista} - {self.nome}'


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
    menor_de_idade = models.BooleanField(default=False)
    vai = models.BooleanField(default=True)
    volta = models.BooleanField(default=True)
    esta_na_ida = models.BooleanField(default=False)
    esta_na_volta = models.BooleanField(default=False)
