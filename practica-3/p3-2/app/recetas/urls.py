from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.index, name='vista_tablas'),
    path('receta/<int:id>', views.receta, name='vista_receta'),
]
