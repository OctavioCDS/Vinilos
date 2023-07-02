from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import (
    Model,
    CharField,
    TextField,
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


