from django.contrib import admin
from .models import Sede, Prueba, Alumno

# Register your models here.

admin.site.register(Sede)
admin.site.register(Prueba)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre')
