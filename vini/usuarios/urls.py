from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('',registro,name='Registro'),
    path('Sesion/',iniciosesion,name='Sesion'),
    path('Sesion_cerrar/',cerrar_sesion,name='Cerrar'),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)