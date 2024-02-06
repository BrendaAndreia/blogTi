from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def processa_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'username': username,
                'password': password,
            }
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
        return render(request, 'autenticacao/login.html', context)
    
    return render(request, 'autenticacao/login.html')

def processa_logout(request):
    logout(request)
    return redirect('login')

def processa_redirect_home(request):
    return redirect('home')