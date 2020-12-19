from django.forms import ModelForm
from users.models import(
    custom_user
)
from core.models import (
    Turma,
    Aluno,
)
from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'
    #input_formats = ['%y-%m-%dT%H:%M']
    # format = '%y-%m-%dT%H:%M'
    pass
# turma


class Turmaform(ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'local']


class GerenciarTurmaForm(forms.Form):
    username = forms.CharField(required=True)


# dia

class DiaForm(forms.Form):
    data = forms.DateField(
        required=True, widget=DateInput(format='%Y-%m-%dT%H:%M'))

# alunos


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['vai', 'volta', 'esta_na_ida', 'esta_na_volta']


class AlunoMenorForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['vai', 'volta']


class AlunoMenorFormMotorista(ModelForm):
    class Meta:
        model = Aluno
        fields = ['esta_na_ida', 'esta_na_volta']


class UsuarioUpdate(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'telefone', 'local']
