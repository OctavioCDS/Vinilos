from django.shortcuts import render, redirect
from sweetify import info, success, warning, error
from .models import Cancion

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Catalogo(request):
    cancion = Cancion.objects.all()
    return render(request,'tienda/catalogo.html',{'cancion': cancion})

def buscador(request):
    nombre = request.GET.get("buscador")
    canciones = Cancion.objects.filter(nombre__icontains=nombre)
    return render(request, 'tienda/catalogo.html', {'cancion': canciones})
