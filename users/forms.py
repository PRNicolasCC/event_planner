from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario


class OrganizadorLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full bg-[#e8f0fe] rounded-xl py-3 px-4 text-gray-900',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full bg-[#e8f0fe] rounded-xl py-3 px-4 text-gray-900',
            'placeholder': 'Contraseña'
        })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        
        if username:
            try:
                user = Usuario.objects.get(email=username)
                if not user.es_proveedor:
                    raise forms.ValidationError(
                        'No tienes permisos de organizador para acceder.',
                        code='not_organizador'
                    )
            except Exception:
                pass
        
        return cleaned_data


class RegistroUsuarioForm(UserCreationForm):
    TIPO_USUARIO = (
        ('cliente', 'Cliente'),
        ('proveedor', 'Proveedor'),
    )

    email = forms.EmailField(label='Correo electrónico')
    tipo_usuario = forms.ChoiceField(
        choices=TIPO_USUARIO,
        label='Tipo de usuario'
    )

    class Meta:
        model = Usuario
        fields = ['email', 'tipo_usuario', 'password1', 'password2']

    def save(self, commit=True):
        usuario = super().save(commit=False)

        tipo_usuario = self.cleaned_data['tipo_usuario']

        if tipo_usuario == 'proveedor':
            usuario.es_proveedor = True
            usuario.es_cliente = False
        else:
            usuario.es_cliente = True
            usuario.es_proveedor = False

        if commit:
            usuario.save()

        return usuario