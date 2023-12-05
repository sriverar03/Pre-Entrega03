from django import template
from django.shortcuts import render
from AppCoder.forms import ClienteFormulario



def inicio_view(xx):
    return render(xx, "AppCoder/inicio.html")

def datos_view(xx): 
      
    miformulario = ClienteFormulario()
    return render(xx, "AppCoder/formulario.html",{"form": miformulario})



def destino_view(xx):
    return render(xx, "AppCoder/destino.html")
