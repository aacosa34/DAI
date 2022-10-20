from django.contrib import admin
from .models import Ingrediente, Receta, Image

# Register your models here.

# Lista para registrar los modelos en el admin
models = [Receta, Image, Ingrediente]

admin.site.register(models)