from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserForm

def inicio(request):
    return render(request, 'inicio.html', {})

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def registrar(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserForm()
    return render(request, 'usuarios/registrar.html', {'form':form})

def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:              
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/ingresar.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')