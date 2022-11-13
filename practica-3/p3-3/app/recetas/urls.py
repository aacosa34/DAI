from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.index, name='vista_tablas'),
    path('receta/<int:id>', views.receta, name='vista_receta'),
    path('receta/new', views.nueva_receta, name='vista_nueva_receta'),
    path('receta/edit/<int:id>', views.editar_receta, name='vista_editar_receta'),
]
