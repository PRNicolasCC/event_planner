from django import forms
from .models import Servicio


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
            'categoria',
            'ciudad',
            'precio_referencia',
            'telefono_contacto',
        ]