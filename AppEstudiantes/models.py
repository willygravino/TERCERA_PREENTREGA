from django.db import models

class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=40)
    apellido_estudiante = models.CharField(max_length=40)
    email_estudiante = models.EmailField() 
