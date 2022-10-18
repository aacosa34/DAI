from django.contrib import admin
from .models import Receta, Image

# Register your models here.

# Lista para registrar los modelos en el admin
models = [Receta, Image]

admin.site.register(models)