# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENEROS)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Mascota(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENEROS)
    cedula = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
