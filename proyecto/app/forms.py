from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario 

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario

        fields = [
            'nombre',
            'apellido',
            'pais',
            'edad'
        ]
        
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'pais' : 'País',
            'edad' : 'Edad'
        }
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
            'pais' : forms.TextInput(attrs={'class' : 'form-control'}),
            'edad' : forms.NumberInput(attrs={'class' : 'form-control'})        
        }
        
        

class FormularioRegistroUsuario(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Correo Electrónico'}))
    first_name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. Solo puedes usar letras, números y los símbolos @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repetir contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Para verificar, introduzca la misma contraseña anterior.</small></span>'
