from django.shortcuts import render
from recetas.models import Receta

# Create your views here.

def index(request):
    request.session['theme'] = 'dark'

    return render(request, 'recetas/base.html', {'titulo': 'Recetas'})

def busqueda(request):
    if request.method == 'GET' and 'busqueda' in request.GET:
        recetas = Receta.objects.filter(nombre__startswith=request.GET['busqueda']).values()
    else:
        recetas = {}

    return render(request, 'recetas/lista_recetas.html', {'titulo': 'Recetas', 'recetas': recetas})
