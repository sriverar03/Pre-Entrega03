from django.urls import path
from django.http import HttpResponse

from AppCoder.views import inicio_view,datos_view,destino_view



urlpatterns = [    
    path("inicio/", inicio_view,name="home"),
    path("formulario/", datos_view,name="new"),
    path("destino/", destino_view,name="destino"),
]