from django.shortcuts import render

# Create your views here.

def index(request):
    oscuro = ''
    return render(request, 'recetas/lista_recetas.html', {'titulo': 'Recetas', 'recetas': '', 'oscuro': oscuro})
