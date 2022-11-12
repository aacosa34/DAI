from django.shortcuts import render, redirect
from django.contrib import messages
from recetas.forms import RecetaForm, CreateUserForm, LoginUserForm
from recetas.models import Ingrediente, Receta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']

        if 'borrarReceta' in request.POST and request.user.is_authenticated:
            receta = Receta.objects.get(id=request.POST['borrarReceta'])
            receta.delete()
            messages.success(request, 'Receta borrada correctamente')
            return redirect('index')
        else:
            messages.error(request, 'No se ha podido borrar la receta: no estás registrado')

    # Si todavía no se ha buscado nada, se muestran todas
    recetas = Receta.objects.all().values()
    cabecera = 'Todas las recetas'
    # Si se ha buscado y se encuentra algo, se muestran las recetas que coincidan
    if 'busqueda' in request.GET:
        cabecera = f"Recetas que contienen '{request.GET['busqueda']}'"
        recetas = Receta.objects.filter(
            nombre__startswith=request.GET['busqueda']).values()

    return render(request, 'recetas/index.html', {'titulo': 'Recetas', 'theme': check_theme(request), 'recetas': recetas, 'cabecera': cabecera, 'user': request.user})

def receta(request, id):
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']

    receta = Receta.objects.get(id=id)    
    ingredientes = Ingrediente.objects.filter(receta=receta).values()

    return render(request, 'recetas/vista_receta.html', {'titulo': receta.nombre, 'receta': receta, 'ingredientes': ingredientes, 'theme': check_theme(request)})

@login_required
def nueva_receta(request):
    form = RecetaForm()
    if request.method == 'POST':
        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']
    
        else:
            form = RecetaForm(request.POST, request.FILES)
            if form.is_valid():
                receta = form.save()
                return redirect('vista_receta', id=receta.pk)

    return render(request, 'recetas/nueva_receta.html', {'titulo': 'Añadir receta', 'form': form, 'theme': check_theme(request)})

@login_required
def editar_receta(request, id):
    receta = Receta.objects.get(id=id)
    form = RecetaForm(instance=receta)
    if request.method == 'POST':
        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']
        
        else:
            form = RecetaForm(request.POST, request.FILES, instance=receta)
            if form.is_valid() and form.has_changed():
                form.save()
                messages.success(request, 'Receta editada correctamente')
                return redirect('vista_receta', id=id)
    
    return render(request, 'recetas/editar_receta.html', {'titulo': 'Editar receta', 'form': form, 'receta': receta, 'theme': check_theme(request)})
            

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']
        else:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se ha registrado correctamente')
                return redirect('login')


    return render(request, 'accounts/register.html',
    {
        'titulo': 'Registrarse',
        'form': form,
        'theme': check_theme(request),
    })

def loginPage(request):
    form = LoginUserForm()
    if request.method == 'POST':
        if 'theme' in request.POST:
            request.session['theme'] = request.POST['theme']

        else:
            usern = request.POST['username']
            passw = request.POST['password']

            user = authenticate(request, username=usern, password=passw)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form = LoginUserForm(request.POST)
                messages.info(request, 'Nombre de usuario o contraseña incorrecto')
                return render(request, 'accounts/login.html', {'titulo':'Iniciar sesión', 'form':form, 'theme':check_theme(request)})

    return render(request, 'accounts/login.html',
    {
        'titulo': 'Iniciar sesión',
        'form':form,
        'theme': check_theme(request),
    })

def logoutUser(request):
    logout(request)
    return redirect('index')

# Funcion auxiliar que comprueba el tema actual
def check_theme(request):
    if 'theme' in request.session:
        return request.session['theme']
    else:
        request.session['theme'] = 'light'
        return request.session['theme']