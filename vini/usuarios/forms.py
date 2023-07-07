from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm,EmailInput,BooleanField,CheckboxInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

class Registro(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = {'class':'form-control'}
        self.fields['password2'].widget.attrs = {'class':'form-control'}
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }
class InicioSesion(Form):
    usuario = CharField(
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Usuario'
            }
        )
    )
    passw = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(

        )
    )