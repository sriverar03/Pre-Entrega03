from django.db import models

# Create your models here.

class Cliente(models.Model):
     nombre = models.CharField(max_length=100)
     apellido = models.CharField(max_length=100)
     
     def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Paises(models.Model):
     nombre = models.CharField(max_length=100)
     
     def __str__(self):
          return self.nombre
     
class Viajes(models.Model):
    Fecha = models.DateField()    
    Cliente =models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    Pais =models.ForeignKey(Paises, on_delete=models.SET_NULL, null=True, blank=True)
     
