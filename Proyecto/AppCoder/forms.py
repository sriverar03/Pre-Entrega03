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


class ViajesFormulario(forms.ModelForm):
    class Meta:
        model = models.Viajes
        fields =["Fecha", "Cliente", "Pais"]
    
        widgets = { 
            "Fecha" : forms.DateInput(attrs={'type': 'date','class':'form-control'}),          
            "Cliente" :forms.Select(attrs={'class':'form-control'}),
            "Pais" : forms.Select(attrs={'class':'form-control'})  
            
        }
