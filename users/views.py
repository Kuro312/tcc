from django.shortcuts import render, redirect
from users.forms import UserForm, UserLoginForm
from users.models import custom_user
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,)
import datetime
# Create your views here.


# sair
def sair(request):
    logout(request)
    return redirect('user:user_login')


# login
def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        u = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if u is not None:
            login(request, u)
            if u.permissao == 1:
                return redirect('core_aluno_home')
            elif u.permissao == 2:
                return redirect('core_home')
        c = {
            'form': form,
            'error': True
        }
        return render(request, 'users/login.html', c)

    c = {
        'form': form,
    }
    return render(request, 'users/login.html', c)


# registrar
def user_register(request):
    form = UserForm()
    if request.method == 'POST':

        form = UserForm(request.POST)
        #form.permissao = request.POST['permissao']
        valido = False
        if form.is_valid():
            valido = True
            u = form.save(commit=False)
            u.date_joined = datetime.date.today()
            u.permissao = request.POST['permissao']
            u.save()
        c = {
            'form': form,
        }
        if valido:
            c['sucesso'] = True
        else:
            c['erro'] = True
        return render(request, 'users/register.html', c)
        # return redirect('user_login')

    c = {
        'form': form,
    }
    return render(request, 'users/register.html', c)
