from django.urls import path
from django.http import HttpResponse

from AppCoder.views import inicio_view,crear_cliente_view,destino_view,buscar_cliente_view,crear_pais_view,buscar_pais_view


urlpatterns = [    
    path("inicio/", inicio_view,name="home"),
    path("cliente/", crear_cliente_view,name="new"),
    path("destino/", destino_view,name="destino"),
    path("buscarcliente/", buscar_cliente_view, name="buscarcliente"),
    path("nuevopais/", crear_pais_view,name="nuevopais"),
    path("buscarpais/", buscar_pais_view, name="buscarpais"),
]