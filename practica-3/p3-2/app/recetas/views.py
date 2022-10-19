from django.shortcuts import render
from recetas.models import Receta

# Create your views here.

def index(request):
    if request.method == 'GET':
        oscuro = request.GET.get('oscuro')
    else:
        oscuro = ''
    return render(request, 'recetas/base.html', {'titulo': 'Recetas', 'oscuro': oscuro})

def vista_tablas(request):
    if request.method == 'GET':
        oscuro = request.GET.get('oscuro')
    else:
        oscuro = ''
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'titulo': 'Recetas', 'recetas': recetas, 'oscuro': oscuro})
