from django.shortcuts import render, redirect
from .forms import Registro,InicioSesion,Modificacion,RegistroA
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from sweetify import info, success, warning, error
from django.contrib.auth.decorators import login_required

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

@login_required
def listadoUsers(request):
    try:
        if request.user.is_authenticated and request.user.is_superuser or request.user.roles.rol == 'Admin':
            usuarios = Usuario.objects.all()
            for usuario in usuarios:
                if not usuario.foto_usuario:
                    usuario.foto_usuario = settings.MEDIA_URL + 'default.jpg'
                    usuario.save()
            return render(request, 'admin/listausers.html', {'usuarios': usuarios})
        else:
            return redirect('Principal')
    except AttributeError:
        return redirect('Principal')

def buscadorU(request):
    username = request.GET.get("username")
    usuarios = Usuario.objects.filter(username__icontains=username)
    return render(request, 'admin/listausers.html', {'usuarios': usuarios})

def modificar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        form = Modificacion(data=request.POST, files=request.FILES, instance=usuario)
        if form.is_valid():
            usuario.roles = form.cleaned_data['rol']
            usuario.save()
            success(request, 'El usuario se ha modificado correctamente')
            return redirect('ListaU')
    else:
        form = Modificacion(instance=usuario)

    contexto = {'form': form}
    return render(request, 'user/Modificar.html', contexto)

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    success(request, 'Usuario Eliminado correctamente.. :D')
    return redirect("ListaU")

def agregar_usuarioA(request):
    try:
       if request.user.is_authenticated and request.user.is_superuser or request.user.roles.rol == 'Admin':
            if request.method == 'POST':
                form = RegistroA(request.POST, request.FILES)
                if form.is_valid():
                    usuario = form.save(commit=False)
                    usuario.roles = form.cleaned_data['rol']
                    usuario.save()
                    success(request, 'El Usuario se ha agregado correctamente :D')
                    return redirect('ListaU')
            else:
                form = RegistroA()

            contexto = {'form': form}
            return render(request, 'user/AgregarU.html', contexto)
    except AttributeError:
        return redirect('Principal')


