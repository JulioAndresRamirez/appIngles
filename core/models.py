from django.db import models
from datetime import datetime
# Create your models here.

#from . import choices


# Create your models here.

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=255, verbose_name='Nombre Sede')
    direccion = models.CharField(max_length=255, verbose_name='Direccion Sede')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        ordering = ['nombre_sede']

    def __str__(self):
        return '{}'.format(self.nombre_sede)


class Prueba(models.Model):
    # tipo_prueba = models.CharField('Tipo de test', max_length=255, choices=choices.TEST_GROUP, default=choices.toeic)
    tipo_prueba = models.CharField('Tipo de test', max_length=255, null=True, blank=True)
    sala = models.CharField('Sala', max_length=255, null=True, blank=True)
    docente = models.CharField('Docente', max_length=255, null=True, blank=True)
    fecha_prueba = models.DateField('Fecha de la prueba')
    hora_inicio = models.DateTimeField('Hora inicio',null=True, blank=True)
    hora_fin = models.DateTimeField('Hora Fin', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    sede = models.ForeignKey(Sede, verbose_name='Sede',related_name='Pruebas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'
        ordering = ['created']

    def __str__(self):
        return '{}, Fecha: {}'.format(self.tipo_prueba, self.fecha_prueba)


class Alumno(models.Model):
    """Modelo Alumnos - Representa una alumno de Duoc UC Melipilla """

    # DATABASE FIELDS
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Identificador')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    carrera = models.CharField(max_length=255, verbose_name="Carrera")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    prueba = models.ForeignKey(Prueba, verbose_name='Prueba', related_name='Alumnos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['created']

    def __str__(self):
        return "{} - {}".format(self.rut, self.nombre)
