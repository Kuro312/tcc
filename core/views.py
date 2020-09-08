from django.shortcuts import render, redirect
from core.forms import (
    Turmaform,
    GerenciarTurmaForm,
    DiaForm,
    AlunoForm,
)
from core.models import (
    Turma,
    Dia,
    Aluno,
)
from users.models import custom_user
import datetime
# Create your views here.

# area do motorista
# home


def core_home(request):
    c = {

    }
    return render(request, 'core/index.html', c)

# turma

# Criação e listagem das turmas do motorista logado


def core_turma_lista(request):
    if request.method == 'POST':
        u = Turma(motorista=request.user, vagas=request.POST['vagas'])
        u.save()
        return redirect('core_turma_lista')
    form = Turmaform()
    turmas = Turma.objects.filter(motorista=request.user)
    c = {
        'form': form,
        'turmas': turmas,
    }
    return render(request, 'core/turma/turma_lista.html', c)

# gerenciamento de uma turma especifica


def core_gerenciar_turma(request, id):
    turma = Turma.objects.get(id=id)
    dias = Dia.objects.filter(turma=turma)
    if request.method == 'POST':

        nome = request.POST['username']
        try:
            u = custom_user.objects.get(username=nome)
        except custom_user.DoesNotExist:
            u = None
        if u is not None:
            turma.alunos.add(u)
        return redirect('core_gerenciar_turma', id)

    alunos = turma.alunos.all()
    form = GerenciarTurmaForm()
    c = {
        'turma': turma,
        'alunos': alunos,
        'form': form,
    }
    return render(request, 'core/turma/gerenciar_turma.html', c)

# apagar uma turma especifica


def core_apagar_turma(request, id):
    turma = Turma.objects.get(id=id)
    if request.method == 'POST':
        turma.delete()

        return redirect('core_turma_lista')

    c = {
        'turma': turma,
    }
    return render(request, 'core/turma/turma_apagar_confirm.html', c)


# lista dos dias de uma turma

def core_lista_dias(request, id):
    turma = Turma.objects.get(id=id)
    if(turma.motorista != request.user):
        return redirect('core_home')

    if request.method == 'POST':
        dia = Dia(data=request.POST['data'], turma=turma)
        dia.save()
        return redirect('core_lista_dias', id)
    dias = Dia.objects.filter(turma=turma).filter(ativo=True)
    form = DiaForm(
        initial={'data': datetime.date.today().strftime('%Y-%m-%d')})
    c = {
        'dias': dias,
        'form': form,

    }
    return render(request, 'core/turma/lista_turma_dia.html', c)

# gerenciar dia especifico


def core_gerenciar_dia(request, id):
    dia = Dia.objects.get(id=id)
    if request.method == 'POST':
        dia.ativo = False
        dia.save()
        return redirect('core_lista_dias', dia.turma.id)
    alunos = Aluno.objects.filter(dia=dia)

    c = {
        'dia': dia,
        'alunos': alunos,

    }
    return render(request, 'core/turma/gerenciar_turma_dia.html', c)


# lista dos dias arquivados


def core_aluno_dia_arquivado_lista(request, idTurma):
    turma = Turma.objects.get(id=idTurma)
    dias = Dia.objects.filter(turma=turma).filter(ativo=False)
    c = {
        'dias': dias,
    }

    return render(request, 'core/turma/dia_arquivado.html', c)

# gerenciar dia arquivado


def core_aluno_dia_arquivado_gerenciar(request, idDia):
    dia = Dia.objects.get(id=idDia)
    alunos = Aluno.objects.filter(dia=dia)
    c = {
        'alunos': alunos,
    }
    return render(request, 'core/turma/dia_arquivado_gerenciar.html', c)

# alunos

# home do aluno


def core_aluno_home(request):
    c = {

    }
    return render(request, 'core/aluno/home/aluno_home.html', c)


# lista das turmas do aluno
def core_aluno_lista_turma(request):
    turmas = Turma.objects.all().filter(alunos=request.user)

    c = {
        'turmas': turmas,
    }
    return render(request, 'core/aluno/turma/aluno_turma_lista.html', c)

# gerenciar uma turma especifica


def core_aluno_turma_gerenciar(request, idTurma):
    turma = Turma.objects.get(id=idTurma)
    dias = Dia.objects.filter(turma=turma).filter(ativo=True)

    c = {
        'turma': turma,
        'dias': dias,
    }
    return render(request, 'core/aluno/turma/aluno_turma_gerenciar.html', c)

# gerenciar um dia especifico


def core_aluno_dia_gerenciar(request, idDia):
    dia = Dia.objects.get(id=idDia)

    try:
        aluno = Aluno.objects.get(usuario=request.user, dia=dia)
    except Aluno.DoesNotExist:
        aluno = None
    if aluno is not None:
        form = AlunoForm(instance=aluno)
    else:
        form = AlunoForm()
    if request.method == 'POST':

        if aluno is not None:
            f = AlunoForm(request.POST, instance=aluno)
            if f.is_valid():
                f.save()
        else:
            f = AlunoForm(request.POST)
            if f.is_valid():
                uf = f.save(commit=False)
                uf.dia = dia
                uf.usuario = request.user
                uf.save()

        return redirect('core_aluno_turma_gerenciar', dia.turma.id)

    c = {
        'dia': dia,
        'form': form,
        'aluno': aluno,
    }
    return render(request, 'core/aluno/turma/dia_gerenciar.html', c)
