from django.db import models


# Create your models here.


class Alumno(models.Model):
    """Modelo Alumnos - Representa una alumno de Duoc UC Melipilla """

    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Numero Identificador')
    nombre = models.CharField(max_length=255, verbose_name='Nombre del estudiante')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
