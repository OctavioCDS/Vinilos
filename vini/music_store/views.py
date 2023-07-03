from django.shortcuts import render, redirect
from sweetify import info, success, warning, error
from .models import Cancion
from .CarritoCompra import Carrito

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Catalogo(request):
    cancion = Cancion.objects.all()
    return render(request,'tienda/catalogo.html',{'cancion': cancion})
def Carro(request):
    return render(request,'tienda/carro.html')

def buscador(request):
    nombre = request.GET.get("buscador")
    canciones = Cancion.objects.filter(nombre__icontains=nombre)
    return render(request, 'tienda/catalogo.html', {'cancion': canciones})

def agregar_cancion(request,cancion_id):
    carrito = Carrito(request)
    cancion = Cancion.objects.get(id=cancion_id)
    carrito.agregar(cancion)
    return redirect('Carro')
def eliminar_cancion(request,cancion_id):
    carrito = Carrito(request)
    cancion = Cancion.objects.get(id=cancion_id)
    carrito.eliminar(cancion)
    return redirect('Carro')
def restar_cancion(request,cancion_id):
    carrito = Carrito(request)
    cancion = Cancion.objects.get(id=cancion_id)
    carrito.restar(cancion)
    return redirect('Carro')
def limpiar_carro(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return redirect('Carro')

