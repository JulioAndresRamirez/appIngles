# Django
from django.shortcuts import render
from django.contrib import messages

# Models
from .models import Alumno, Prueba, Sede


# Create your views here.

def index(request):
    """Vista inicial"""

    if 'buscar_alumno' in request.POST:
        identificador = request.POST['identificador']
        try:
            alumno = Alumno.objects.get(pk=identificador)
        except:
            return render(request, 'core/no_existe.html')


        if alumno is not None:

            return render(request, 'core/resultado.html', {
                'alumno': alumno
            })
        else:
            messages.warning(request, 'Error al encontrar el Alumno.')
            return render(request, 'core/no_existe.html')


    return render(request, 'core/index.html')
