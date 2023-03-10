from django.shortcuts import render
from AppEstudiantes.forms import EstudiantesForm
from AppEstudiantes.models import Estudiante

def Formulario_Estudiantes(request):
    context = {
    "form" : EstudiantesForm(),
    }

    return render(request, "AppEstudiantes/formulario_estudiantes.html",context)

def Agregar_Estudiante (request):
    data_estudiante = EstudiantesForm(request.POST)
    data_estudiante.save()
    
    context = {
    "form" : EstudiantesForm(),
    "Posts": Estudiante.objects.all(),
    }
    return render(request, "AppEstudiantes/formulario_estudiantes.html",context)


