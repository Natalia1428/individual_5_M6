from  django import forms

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