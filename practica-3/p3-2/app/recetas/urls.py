from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('?busqueda=<str:busqueda>', views.vista_tablas, name='vista-tablas'),
]
