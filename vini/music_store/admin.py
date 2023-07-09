from django.contrib import admin
from .models import Genero,Cancion,DetalleComprobante,Comprobante

# Register your models here.
admin.site.register(Genero)
admin.site.register(Cancion)
admin.site.register(DetalleComprobante)
admin.site.register(Comprobante)
