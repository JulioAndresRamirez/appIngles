from django.test import TestCase
from .models import Alumno, Prueba, Sede
from datetime import date, datetime
# Create your tests here.



class AlumnoTestCase(TestCase):

    def setUp(self):
        Sede.objects.create(nombre_sede='Melipilla', direccion='1105, Melipilla')
        #Prueba.objects.create(tipo_prueba='TOEIC', fecha_prueba=date.today(), hora_inicio=datetime.now(), hora_fin=datetime.now(), sede=1)
        #Alumno.objects.create(rut='22606030-8', nombre='Julio Ramirez', carrera='Ing. Informática', prueba=0)


    def test_alumnos_save(self):
        alumns = Alumno.objects.all()
        print(alumns)

