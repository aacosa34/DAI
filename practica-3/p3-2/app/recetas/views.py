from django.shortcuts import render
from recetas.models import Receta

# Create your views here.

def index(request):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']
    
    if 'theme' not in request.session:
        request.session['theme'] = 'light'

    return render(request, 'recetas/index.html', {'titulo': 'Recetas', 'theme': request.session['theme']})

def busqueda(request):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']

    if 'theme' in request.session:
        theme = request.session['theme']
    else:
        request.session['theme'] = 'light'

    if request.method == 'GET' or 'busqueda' in request.GET:
        recetas = Receta.objects.filter(nombre__startswith=request.GET['busqueda']).values()
    else:
        recetas = {}

    return render(request, 'recetas/lista_recetas.html', {'titulo': 'Recetas', 'recetas': recetas, 'theme': theme})

def receta(request, id):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']

    if 'theme' in request.session:
        theme = request.session['theme']
    else:
        request.session['theme'] = 'light'

    receta = Receta.objects.get(id=id)    

    return render(request, 'recetas/vista_receta.html', {'titulo': 'Recetas', 'receta': receta, 'theme': theme})