from django import forms
from . import models

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nombre', 'apellido']
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))



class PaisFormulario(forms.ModelForm):
    class Meta:
        model = models.Paises
        fields = ['nombre']
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   