from django import forms
from AppEstudiantes.models import Estudiante, Profe, Curso

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model =  Estudiante
        fields = '__all__'

class ProfesForm(forms.ModelForm):
    class Meta:
        model =  Profe
        fields = '__all__'

class CursosForm(forms.ModelForm):
    class Meta:
        model =  Curso
        fields = '__all__'





