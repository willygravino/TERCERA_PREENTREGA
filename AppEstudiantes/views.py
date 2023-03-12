from django.shortcuts import render
from AppEstudiantes.forms import EstudiantesForm, ProfesForm, CursosForm
from AppEstudiantes.models import Estudiante, Profe, Curso
from django.urls import reverse_lazy

def Principal(request):
    return render(request, "AppEstudiantes/index.html")

def Agregar_Estudiante(request):
    if request.method == "POST":
        data_estudiante = EstudiantesForm(request.POST)
        if EstudiantesForm(request.POST).is_valid():
            data_estudiante = EstudiantesForm(request.POST)
            data_estudiante.save()
            context = {
                "form" : EstudiantesForm(),
                "Posts": Estudiante.objects.all(),
         }
            success_url = reverse_lazy("agregar_estudiante")

            return render(request, "AppEstudiantes/index.html",context) 
  
    else:
        context = {
            "form" : EstudiantesForm(),
            "Posts": Estudiante.objects.all(),
         }
    return render(request, "AppEstudiantes/formulario_estudiantes.html",context)

def Buscar_Estudiante(request):
       criterio = request.GET.get("criterio")
       contexto = {
            "Posts": Estudiante.objects.filter(nombre_estudiante__icontains=criterio).all(),
          }
       return render(request, "AppEstudiantes/busqueda_estudiante.html",contexto)

def Buscar_Estudiante_aparte(request):
       criterio = request.GET.get("criterio")
       contexto = {
            "Posts": Estudiante.objects.filter(nombre_estudiante__icontains=criterio).all(),
          }
       return render(request, "AppEstudiantes/busqueda_aparte.html",contexto)


def Agregar_Profe(request):
    if request.method == "POST":
        data_profe = ProfesForm(request.POST)
        if ProfesForm(request.POST).is_valid():
            data_profe = ProfesForm(request.POST)
            data_profe.save()
            context = {
                "form" : ProfesForm(),
                "Posts": Profe.objects.all(),
         }
            return render(request, "AppEstudiantes/index.html",context) 
  
    else:
        context = {
            "form" : ProfesForm(),
            "Posts": Profe.objects.all(),
         }
    return render(request, "AppEstudiantes/formulario_profes.html",context)

def Agregar_Curso(request):
    if request.method == "POST":
        data_profe = CursosForm(request.POST)
        if CursosForm(request.POST).is_valid():
            data_curso = CursosForm(request.POST)
            data_curso.save()
            context = {
                "form" : CursosForm(),
                "Posts": Curso.objects.all(),
         }
            return render(request, "AppEstudiantes/index.html",context) 
  
    else:
        context = {
            "form" : CursosForm(),
            "Posts": Curso.objects.all(),
         }
    return render(request, "AppEstudiantes/formulario_cursos.html",context)
