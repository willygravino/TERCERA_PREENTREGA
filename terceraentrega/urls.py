"""terceraentrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppEstudiantes.views import Agregar_Estudiante, Principal, Buscar_Estudiante, Agregar_Profe, Agregar_Curso, Buscar_Estudiante_aparte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal', Principal, name="pagina-principal"),
    path('gestionestudiantes', Agregar_Estudiante, name="agregar-estudiante"),
    path('gestionesprofes', Agregar_Profe, name="agregar-profe"),
    path('gestionescurso', Agregar_Curso, name="agregar-curso"),
    path('buscarestudiante/', Buscar_Estudiante, name="buscar-estudiante"),
    path('busquedaaparte/', Buscar_Estudiante_aparte, name="busqueda-aparte"),
 
]

