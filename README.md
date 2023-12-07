# Pre-Entrega03

## Configuración inicial
### 1. Crear carpeta para nuestro repositorio, "Pre-Entrega03"
### 2. Crear archivo README.md
### 3. Instalar django: pip install django
### 4. Crear proyecto: django-admin startproject Proyecto
### 5. Dentro de la carpeta Proyecto/ crear aplicación python manage.py startapp AppCoder
### 6. Registrar la aplicación en Proyecto/settings.py
### 7. Ejecutar python manage.py runserver para inciar servidor web


# Configurar Rutas:

Incluir rutas aplicacion AppCoder en  Proyecto/urls.py

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/67e3e0eb-3ee0-433b-aa56-89cbd3ec7216)


# Pasos en AppCoder

Crear vistas en view.py Ejemplo:

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/260fb0ba-160a-4a9c-82d5-5a1ebf800401)


Despues se deben crear las rutas en AppCoder/urls.py

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/d24ea5be-b0e2-43de-b6c5-4a77a3378a27)

Crear carpeta templates/AppCoder con pagina html

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/8c539d01-5da9-4ca7-919b-d5312e96122a)

se crean herencias  dentro de templates en la pagina inicial "inicio.html".

{% load static %}   --->    <b>permite cargar la carpeta static</b><br>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <link href="{% static 'bootstrap/css/bootstrap.min.css'  %}" rel="stylesheet" />  --->    <b>se tiene acceso bootstrap 5</b><br>
  </head>
  <body><br>
    {% include "AppCoder/layout/header.html" %}   --->    <b>se inyecta header "navabar" en las páginas</b> <br>
    {% block contenidoPrincipal %}   --->    <b>el contenido se cambiará en forma dinamica a travez de la herencia</b> <br>
        
    <div class="row"> 
      <div class="col-10 mx-auto">
             <h1>SISTEMA DE VIAJES</h1> 
      </div>
    </div>    
    {% endblock %}

    <script src="{% static 'bootstrap/js/bootstrap.min.js'  %}"></script>   --->    <b>se accede a bootstrap.js</b> <br>
  </body>
</html>

Se tiene acceso a herencia de las demás páginas agregando siguiente contenido:

{% load static %} <br>
{% extends "AppCoder/inicio.html" %} <br>
{% block contenidoPrincipal %} --->    <b>herencia para el cambio de contenido principal de la página de inicio</b><br> 
  --->    <b>dentro del block debe estar el contenido de la página</b>   <--- <br>
{% endblock %}

## Base de datos dbsqlite3

En Appcoder crear los modelo relacional ena archivo models.py

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/c42e63ec-cf0f-4b57-806c-3750792ad2da)

Crear formularios dinamicos en archivo forms.py

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/57e95955-a5b9-4cc6-984c-f4258f993361)

Por ultimo se crea carpeta static para añadir estilo a las diferentes páginas html, utizando bootstrat 5

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/9b5e8a8d-0be8-405b-b58c-ea11c42224b3)

Ejemplo:

![image](https://github.com/sriverar03/Pre-Entrega03/assets/95256304/e46ff51f-5333-4cd9-a6e6-ff947d82f2de)









