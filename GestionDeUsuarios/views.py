from django.shortcuts import render

def mostrar_mi_template(request):
    return render(request, "GestionDeUsuarios/index.html")
    