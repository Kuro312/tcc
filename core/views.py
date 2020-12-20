from django.shortcuts import render, redirect
from core.forms import (
    Turmaform,
    GerenciarTurmaForm,
    DiaForm,
    AlunoForm,
    AlunoMenorForm,
    AlunoMenorFormMotorista,
    UsuarioUpdate
)
from core.models import (
    Turma,
    Dia,
    Aluno,
)
from users.models import custom_user
import datetime
from decouple import config

# Create your views here.

# area do motorista
# home


def core_home(request):

    c = {

    }
    return render(request, 'core/index.html', c)

# turma

#  listagem das turmas do motorista logado


def core_turma_lista(request):

    turmas = Turma.objects.filter(motorista=request.user)
    c = {

        'turmas': turmas,
    }
    return render(request, 'core/turma/turma_lista.html', c)


# cadastrar turma

def core_turma_cadastrar(request):
    if request.method == 'POST':
        # u = Turma(motorista=request.user,nome = request.POST['nome'], local = request.POST['local'])

        # u.save()
        form = Turmaform(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.motorista = request.user
            u.save()

        return redirect('core_turma_lista')
    form = Turmaform()

    c = {
        'form': form,
    }
    return render(request, 'core/turma/cadastrar_turma.html', c)

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
        'dia': dia,
    }
    return render(request, 'core/turma/dia_arquivado_gerenciar.html', c)


def core_turma_dia_gerenciar(request, idDia, idAluno):
    dia = Dia.objects.get(id=idDia)
    aluno = Aluno.objects.get(id=idAluno)
    form = AlunoMenorFormMotorista(instance=aluno)
    if request.method == "POST":
        f = AlunoMenorFormMotorista(request.POST, instance=aluno)
        if f.is_valid():
            f.save()
        return redirect('core_gerenciar_dia', idDia)
    c = {
        'form': form,
    }
    return render(request, 'core/turma/turma_dia_gerenciar.html', c)


def core_turma_dia_rota(request, idDia):
    dia = Dia.objects.get(id=idDia)
    alunos = Aluno.objects.filter(dia=dia)
    local_motorista = dia.turma.motorista.local
    destino = dia.turma.local
    locais = []

    for aluno in alunos:
        locais.append([aluno.usuario.local[0], aluno.usuario.local[1]])

    mapbox_key = config('MAPBOX_KEY')

    c = {
        'alunos': alunos,
        'locais': locais,
        'local_motorista': local_motorista,
        'destino': destino,
        'mapbox_key': mapbox_key,
    }

    return render(request, 'core/turma/dia_rota.html', c)


def core_motorista_atualizar(request, id):
    usuario = custom_user.objects.get(id=id)

    if request.method == "POST":
        print(request.POST)
        form = UsuarioUpdate(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('core_aluno_home')
    form = UsuarioUpdate(instance=usuario)
    c = {
        'form': form,
        'usuario': usuario,
    }
    return render(request, 'core/turma/motorista_update.html', c)

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
    alunos = Aluno.objects.filter(usuario=request.user).filter(dia__in=dias)
    print(alunos)
    alunos_dias = [aluno.dia for aluno in alunos]

    c = {
        'turma': turma,
        'dias': dias,
        'alunos': alunos,
        'alunos_dias': alunos_dias,
    }
    return render(request, 'core/aluno/turma/aluno_turma_gerenciar.html', c)

# gerenciar um dia especifico


def core_aluno_dia_gerenciar(request, idDia):
    menor = False
    hoje = datetime.date.today().year
    data = hoje - 18
    data_usuario = request.user.data_nascimento.year

    if data_usuario > data:
        menor = True

    dia = Dia.objects.get(id=idDia)
    # Indentifica se ja tem um objeto aluno linkado a esse dia e usuario
    try:
        aluno = Aluno.objects.get(usuario=request.user, dia=dia)
    except Aluno.DoesNotExist:
        aluno = None
    # gera o formulario
    if aluno is not None:
        if menor:
            form = AlunoMenorForm(instance=aluno)
        else:
            form = AlunoForm(instance=aluno)

    else:
        if menor:
            form = AlunoMenorForm()
        else:
            form = AlunoForm()
    #
    if request.method == 'POST':

        if aluno is not None:
            if menor:
                f = AlunoMenorForm(request.POST, instance=aluno)
                if f.is_valid():
                    f.save(commit=False)
                    f.menor_de_idade = True
                    f.save()
            else:
                f = AlunoForm(request.POST, instance=aluno)
                if f.is_valid():

                    f.save()
        else:
            if menor:
                f = AlunoMenorForm(request.POST)
                if f.is_valid():
                    uf = f.save(commit=False)
                    uf.dia = dia
                    uf.usuario = request.user
                    uf.menor_de_idade = True
                    uf.save()
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


def core_aluno_atualizar(request, id):
    usuario = custom_user.objects.get(id=id)

    if request.method == "POST":
        form = UsuarioUpdate(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('core_aluno_home')
    form = UsuarioUpdate(instance=usuario)
    c = {
        'form': form,
        'usuario': usuario,
    }
    return render(request, 'core/aluno/aluno_update.html', c)


def core_aluno_rota(request, idDia):
    # dia = Dia.objects.get(id=idDia)
    # usuario = request.user

    dia = Dia.objects.get(id=idDia)
    alunos = Aluno.objects.filter(dia=dia)
    local_motorista = dia.turma.motorista.local
    destino = dia.turma.local
    locais = [aluno.usuario.local for aluno in alunos]
    mapbox_key = config('MAPBOX_KEY')

    c = {
        'alunos': alunos,
        'local_motorista': local_motorista,
        'destino': destino,
        'mapbox_key': mapbox_key,
        'locais': locais,
    }
    return render(request, 'core/aluno/rota/aluno_rota.html', c)
