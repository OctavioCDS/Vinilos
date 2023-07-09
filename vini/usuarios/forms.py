from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm,EmailInput,BooleanField,CheckboxInput,FileInput,ModelChoiceField,Select,fields_for_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Usuario,Rol

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
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class Modificacion(ModelForm):
    rol = ModelChoiceField(queryset=Rol.objects.all(), widget=Select(attrs={'class': 'form-control'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')
        if 'password1' in self.fields:
            self.fields['password1'].required = False

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'foto_usuario']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'rol': Select(attrs={'class': 'form-control'}),
            'foto_usuario': FileInput(attrs={'class': 'form-control'}),
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

class RegistroA(UserCreationForm):
    rol = ModelChoiceField(queryset=Rol.objects.all(), widget=Select(attrs={'class': 'form-control'}), required=False)

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = {'class':'form-control'}
        self.fields['password2'].widget.attrs = {'class':'form-control'}
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email','rol']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'rol': Select(attrs={'class': 'form-control'}),
        }
class RegistroPerfil(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')
        if 'password1' in self.fields:
            self.fields['password1'].required = False

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'foto_usuario']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'foto_usuario': FileInput(attrs={'class': 'form-control'}),
        }