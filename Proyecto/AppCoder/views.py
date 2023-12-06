from django import forms, template
from django.shortcuts import render
from AppCoder.forms import ClienteFormulario
from . import models




def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def crear_cliente_view(request):
    msg=''
    if request.method == 'POST':
        form = ClienteFormulario(request.POST)
        if form.is_valid():
            form.save()
            msg= "Cliente " + request.POST['nombre']+ "  "+ request.POST['apellido']+ " ha sido creado en el Sistema."            
            return render(request, "AppCoder/nuevocliente.html", {'msg': msg,"form": ClienteFormulario()})
    else:      
        miformulario = ClienteFormulario()
        return render(request, "AppCoder/nuevocliente.html",{"form": miformulario,'msg': msg})

def buscar_cliente_view (request):
    
    if request.method == 'POST':
        datos = models.Cliente.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/buscarcliente.html',{'filtro':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarcliente.html')       
        
        
    
    
    

def destino_view(xx):
    return render(xx, "AppCoder/destino.html")



