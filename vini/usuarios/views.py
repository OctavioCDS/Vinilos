from django.shortcuts import render, redirect
from .forms import Registro,InicioSesion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from sweetify import info, success, warning, error

# Create your views here.
def registro(request):
    if request.method == 'GET':
        contexto={
            'formu': Registro()
        }
        return render(request,'user/registro.html',contexto)
    if request.method == 'POST':
        formulario= Registro(data=request.POST)
        es_valido= formulario.is_valid()
        if es_valido:
            nuevo_user = formulario.save()
            success(request,'Gracias por unirte a nosotros,disfruta de nuestro contenido')
            return redirect('Principal')
        contexto={
            'formu': formulario
        }
        warning(request,'Uyy, Ha ocurrido un error con los campos ingresados, verifique..')
        return render(request,'user/registro.html',contexto)
def iniciosesion(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':InicioSesion(),
        }
        return render(request,'user/iniciosesion.html',contexto)
    if request.method == 'POST':
        datos_usuario = InicioSesion(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username = datos_usuario.cleaned_data['usuario'],
                password = datos_usuario.cleaned_data['passw']
            )
            if usuario is not None:
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('Principal')
        warning(request, 'Usuario y contraseña erroneos, revise los campos...')
        contexto = {
            'formulario': datos_usuario
        }
        return render(request,'user/iniciosesion.html', contexto)
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesión cerrada')
    return redirect('Principal')
