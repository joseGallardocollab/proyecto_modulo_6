from django import forms
from .models import Proyecto, Tarea
from datetime import date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.cl'
            }
        ),
        label="Correo electrónico",
        help_text="Ingresa un correo válido para tu cuenta."

    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = "Debe ser único."

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password1'].label = "Contraseña"
        self.fields['password1'].help_text = "Debe tener al menos 8 caracteres."

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['password2'].help_text = "Repite la contraseña para verificar."
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TelInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa tu usuario'
            }
        )
    )
    
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingresa tu contrasena'
                }
            )
        )

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del proyecto',
                'maxlength': '25' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe el proyecto',
                'rows': 3,
                'maxlength': '100'  
            }),
        }


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'prioridad', 'fecha_limite', 'asignado_a'] 
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la tarea',
                'maxlength': '150'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_limite': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local' 
            }),
            'asignado_a': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def _clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite and fecha_limite.date() < date.today():
            raise forms.ValidationError("La fecha límite no puede ser anterior a la fecha actual.")
        return fecha_limite