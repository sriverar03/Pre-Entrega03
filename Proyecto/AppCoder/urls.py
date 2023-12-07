from django.urls import path
from django.http import HttpResponse

from AppCoder.views import listar_paises_view, listar_clientes_view, inicio_view,crear_cliente_view,buscar_cliente_view,crear_pais_view,buscar_pais_view,viajes_view,buscar_viaje_view,listar_viajes_view


urlpatterns = [    
    path("inicio/", inicio_view,name="home"),
    path("cliente/", crear_cliente_view,name="new"),
    path("solicitudViaje/", viajes_view,name="solicitudViaje"),
    path("buscarcliente/", buscar_cliente_view, name="buscarcliente"),
    path("nuevopais/", crear_pais_view,name="nuevopais"),
    path("buscarpais/", buscar_pais_view, name="buscarpais"),
    path("buscarviajes/", buscar_viaje_view, name="buscarviajes"),
    path("listarviajes/", listar_viajes_view, name="listarviajes"),
    path("listarclientes/", listar_clientes_view, name="listarclientes"),
    path("listarpaises/", listar_paises_view, name="listarpaises"),

]