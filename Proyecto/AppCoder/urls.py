from django.urls import path
from django.http import HttpResponse

from AppCoder.views import inicio_view,crear_cliente_view,destino_view,buscar_cliente_view


urlpatterns = [    
    path("inicio/", inicio_view,name="home"),
    path("cliente/", crear_cliente_view,name="new"),
    path("destino/", destino_view,name="destino"),
    path("buscarcliente/", buscar_cliente_view, name="buscarcliente"),
]