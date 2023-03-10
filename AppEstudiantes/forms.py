from django import forms
from AppEstudiantes.models import Estudiante

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model =  Estudiante
        fields = '__all__'




