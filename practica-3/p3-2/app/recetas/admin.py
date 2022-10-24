from django.contrib import admin
from .models import Ingrediente, Receta

# Register your models here.

# Lista para registrar los modelos en el admin
models = [Receta, Ingrediente]

admin.site.register(models)