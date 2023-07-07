from django.db import models
from django.db.models import (
    Model,
    CharField,
    ImageField,
    ForeignKey,
    SET_NULL
)
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class Rol(Model):
    rol = CharField(max_length=50, unique=True, null=False, default='User')

    def __str__(self):
        return self.rol
    



class UsuarioManager(BaseUserManager):
        def create_user(self,email,username,nombre,apellido,password =None):
             if not email:
                  raise ValueError('El usuario debe tener un correo electronico!')
             
             usuario = self.model(
                  username = username,
                  email = self.normalize_email(email),
                  nombre = nombre,
                  apellido = apellido
             )

             usuario.set_password(password)
             usuario.save()
             return usuario
    
class Usuario(AbstractUser):
    foto_usuario = ImageField(upload_to='imagen_usuario/' ,blank=True ,null=True,default='default.jpg')
    roles = ForeignKey (Rol, null=True, blank=True,on_delete=SET_NULL)
