from django.shortcuts import render, redirect
from recetas.forms import RecetaForm
from recetas.models import Ingrediente, Receta

# Create your views here.

def index(request):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']
    
    if 'theme' not in request.session:
        request.session['theme'] = 'light'


    # Si todavía no se ha buscado nada, se muestran todas
    recetas = Receta.objects.all().values()
    mensaje = 'Todas las recetas'
    # Si se ha buscado y se encuentra algo, se muestran las recetas que coincidan
    if 'busqueda' in request.GET:
        mensaje = f"Recetas que contienen '{request.GET['busqueda']}'"
        recetas = Receta.objects.filter(
            nombre__startswith=request.GET['busqueda']).values()

    return render(request, 'recetas/index.html', {'titulo': 'Recetas', 'theme': request.session['theme'], 'recetas': recetas, 'mensaje': mensaje})

def receta(request, id):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']

    if 'theme' in request.session:
        theme = request.session['theme']
    else:
        request.session['theme'] = 'light'

    receta = Receta.objects.get(id=id)    
    ingredientes = Ingrediente.objects.filter(receta=receta).values()

    return render(request, 'recetas/vista_receta.html', {'titulo': receta.nombre, 'receta': receta, 'ingredientes': ingredientes, 'theme': theme})

def nueva_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save()
            return redirect('vista_receta', id=receta.pk)

        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']
    else:
        form = RecetaForm()

    if 'theme' in request.session:
        theme = request.session['theme']
    else:
        request.session['theme'] = 'light'
    

    return render(request, 'recetas/nueva_receta.html', {'titulo': 'Añadir receta', 'form': form,'theme': theme})