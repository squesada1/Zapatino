from django import forms
from apps.usuarios.models import datos_usuarios

class RegistrarUsuario(forms.ModelForm):
    class Meta:
        model = datos_usuarios
        exclude=()
        