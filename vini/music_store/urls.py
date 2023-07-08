from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('',Catalogo,name='Catalogo'),
    path('Carro/',Carro,name='Carro'),
    path('buscador/', buscador, name="buscador"),
    path('agregar/<int:cancion_id>/',agregar_cancion,name='AGG'),
    path('eliminar/<int:cancion_id>/',eliminar_cancion,name='DEL'),
    path('restar/<int:cancion_id>/',restar_cancion,name='RES'),
    path('limpiar/',limpiar_carro,name='CLEAN'),
    path('ListaV/',listadoVinilos,name='ListaV'),
    path('buscadorV/', buscadorV, name="buscadorV"),
    path('ModificarV/<id>', modificar_vinilo, name="ModificarV"),
    path('EliminarV/<id>', eliminar_vinilo, name="EliminarV"),
    path('AgregarV', agregar_vinilo, name="AgregarV"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
