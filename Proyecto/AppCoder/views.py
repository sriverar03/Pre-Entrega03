from django import forms, template
from django.shortcuts import render
from AppCoder.forms import ClienteFormulario,PaisFormulario
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
        
        
def paises_view(request):
    return render(request, "AppCoder/nuevopais.html")  


def crear_pais_view(request):
    msg=''
    if request.method == 'POST':
        form = PaisFormulario(request.POST)
        if form.is_valid():
            form.save()
            msg= "País agregado en el Sistema."            
            return render(request, "AppCoder/nuevopais.html", {'msg': msg,"form": PaisFormulario()})
    else:      
        miformulario = PaisFormulario()
        return render(request, "AppCoder/nuevopais.html",{"form": miformulario,'msg': msg})  
    

def buscar_pais_view (request):
    
    if request.method == 'POST':
        datos = models.Paises.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/buscarpais.html',{'filtro':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarpais.html') 
    
    

def destino_view(xx):
    return render(xx, "AppCoder/destino.html")



