from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout


#Pagina inicial
def home(request):
    return render(request, 'home.html')


#Cadastro de usuarios
def create(request):
    return render(request, 'create.html')


#Inclusão dos dados dos usuarios no Banco de Dados
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas não conferem!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(24)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-sucess'

    return render(request, 'create.html',data)


#Painel de Login
def painel(request):
    return render(request, 'painel.html')


#Pagina prcessamento do Login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html',data)


#Pagina inicio dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#Logout
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')

