from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth import logout as djangoLogout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        if models.User.objects.filter(username=username):
            return render(request, 'users/register.html')
        
        models.User.objects.create(
            username = username,
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            password = request.POST['password']
        )

        return redirect('login')
    
    return render(request, 'autenticacao/register.html')

def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )

        if user:
            djangoLogin(request, user)
            return redirect('allapps')
        else:
            render(request, 'autenticacao/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login.html')

def logout(request):
    djangoLogout(request)
    return redirect('allapps')
