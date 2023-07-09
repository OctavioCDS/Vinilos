from django.db import models
from django.core.validators import MinValueValidator
from usuarios.models import Usuario
from django.db.models import (
    Model,
    CharField,
    ManyToManyField,
    FileField,
    ImageField,
    ForeignKey,
    DateField,
    IntegerField,
    CASCADE
)
# Create your models here


class Genero(Model):
    #id que genera django
    genero = CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genero
    
class Cancion(Model):
    #id que genera django
    nombre = CharField(max_length=100, null=False)
    artistas = CharField(max_length=200,null=False,default='valor_predeterminado')
    imagen = ImageField(upload_to='img/', null=True)
    musica = FileField(upload_to='musica/')
    precio = IntegerField(validators=[MinValueValidator(1000)],null=False,default=1000)
    fecha_publicacion = DateField()
    genero = ForeignKey(Genero,on_delete= CASCADE)

    def __str__(self):
        para = 'cancion:' + ' ' + str(self.nombre)+ ' ' + 'precio:' + str(self.precio) + ' ' + 'artistas:' + str(self.artistas)+ ' ' + 'fecha de publicacion: ' + str(self.fecha_publicacion) 
        return para


class Comprobante(Model):
    #id por django
    cliente = ForeignKey(Usuario,on_delete= CASCADE)
    fecha_compra = DateField(auto_now=True)
    canciones = ManyToManyField(Cancion)
    total = IntegerField(validators=[MinValueValidator(10000000)])

    def __str__(self):
        xd3 = "Cliente: " + str(self.cliente) + " - " + "Total: " + str(self.total) + " - " + "fecha:" + str(self.fecha_compra)
        return xd3


class DetalleComprobante(Model):
    #id por django
    comprobante = ForeignKey(Comprobante, on_delete=CASCADE)
    cancion = ForeignKey(Cancion, on_delete=CASCADE)

    def __str__(self):
        xd3 = "Cancion: " + str(self.cancion) + " - " + "nombre: " + str(self.comprobante)
        return xd3


