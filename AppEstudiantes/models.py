from django.db import models

class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=40)
    apellido_estudiante = models.CharField(max_length=40)
    email_estudiante = models.EmailField() 

class Profe(models.Model):
    nombre_profe = models.CharField(max_length=40)
    apellido_profe = models.CharField(max_length=40)
    email_profe = models.EmailField()
    profesion = models.CharField(max_length=30)

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=40)
    camada = models.CharField(max_length=20)
    