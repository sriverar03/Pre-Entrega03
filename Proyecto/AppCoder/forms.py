from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()