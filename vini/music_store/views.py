from django.shortcuts import render, redirect
from sweetify import info, success, warning, error
from .models import Cancion,Comprobante,DetalleComprobante
from .CarritoCompra import Carrito
from .forms import ModificacionVinilo

from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required
def Catalogo(request):
    cancion = Cancion.objects.all()
    return render(request,'tienda/catalogo.html',{'cancion': cancion})
@login_required
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

#vinilos
@login_required
def listadoVinilos(request):
    try:
        if request.user.is_authenticated and request.user.is_superuser or request.user.roles.rol == 'Admin' or request.user.roles.rol == 'Bodeguero':
            canciones = Cancion.objects.all()
            return render(request, 'admin/listacatalogo.html', {'canciones': canciones})
        else:
            return redirect('Principal')
    except AttributeError:
        return redirect('Principal')


def buscadorV(request):
    nombre = request.GET.get("nombre")
    canciones = Cancion.objects.filter(nombre__icontains=nombre)
    return render(request, 'admin/listacatalogo.html', {'canciones': canciones})

def modificar_vinilo(request, id):
    cancion = Cancion.objects.get(id=id)
    if request.method == "POST":
        form = ModificacionVinilo(data=request.POST, files=request.FILES, instance=cancion)
        if form.is_valid():
            cancion.save()
            success(request, 'El Vinilo se ha modificado correctamente')
            return redirect('ListaV')
    else:
        form = ModificacionVinilo(instance=cancion)

    contexto = {'form': form}
    return render(request, 'tienda/ModificarVinilos.html', contexto)

def eliminar_vinilo(request, id):
    vinilo= Cancion.objects.get(id=id)
    vinilo.delete()
    success(request, 'Vinilo Eliminado correctamente.. :D')
    return redirect("ListaV")

def agregar_vinilo(request):
    try:
       if request.user.is_authenticated and request.user.is_superuser or request.user.roles.rol == 'Admin' or request.user.roles.rol == 'Bodeguero':
            if request.method == 'POST':
                form = ModificacionVinilo(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    success(request, 'El producto se ha agreado correctamente :D')
                    return redirect('ListaV')
            else:
                form = ModificacionVinilo()

            contexto = {'form': form}
            return render(request, 'admin/agregarvinilo.html', contexto)
    except AttributeError:
        return redirect('Principal')
    

@login_required
def generar_comprobante(request):
    carrito = Carrito(request)
    productos = carrito.get_productos()
    total = carrito.total()

    # Crear un objeto Comprobante
    comprobante = Comprobante(cliente=request.user, total=total)
    comprobante.save()

    for producto in productos:
        cancion = Cancion.objects.get(id=producto['cancion_id'])
        detalle_comprobante = DetalleComprobante(comprobante=comprobante, cancion=cancion)
        detalle_comprobante.save()

    carrito.limpiar()

    nombre_cliente = request.user.first_name
    apellido_cliente = request.user.last_name
    correo_cliente = request.user.email

    return render(request, 'tienda/Comprobante.html', {'comprobante': comprobante, 'nombre_cliente': nombre_cliente, 'apellido_cliente': apellido_cliente, 'correo_cliente': correo_cliente})

def listaventas(request):
    try:
        if request.user.is_authenticated and request.user.is_superuser or request.user.roles.rol == 'Admin' or request.user.roles.rol == 'Vendedor':
            comprobantes = Comprobante.objects.all()
            return render(request, 'admin/listaventas.html', {'comprobantes': comprobantes})
        else:
            return redirect('Principal')
    except AttributeError:
        return redirect('Principal') 
    

def buscadorC(request):
    id = request.GET.get("id")
    comprobantes = Comprobante.objects.filter(id__icontains=id)
    return render(request, 'admin/listaventas.html', {'comprobantes': comprobantes})

