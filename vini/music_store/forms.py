from django.forms import Form, CharField, TextInput, ModelForm,FileInput,NumberInput,DateInput,ModelChoiceField,Select
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Cancion,Genero
class ModificacionVinilo(ModelForm):
    genero = ModelChoiceField(queryset=Genero.objects.all(), widget=Select(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = Cancion
        fields = ['nombre', 'artistas', 'imagen', 'musica', 'precio','fecha_publicacion','genero']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Vinilo'
                }
            ),
            'artistas': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'artistas'
                }
            ),
            'imagen': FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'musica': FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'audio'
                }
            ),
            'precio': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'precio'
                }
            ),
            'fecha_publicacion': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'fecha de publicacion'
                }
            ),
            'genero': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona un Genero'
                }
            ),

        }