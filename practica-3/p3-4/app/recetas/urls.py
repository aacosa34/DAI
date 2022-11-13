from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('buscar', views.index, name='vista_tablas'),
    path('receta/<int:id>', views.receta, name='vista_receta'),
    path('receta/new', views.nueva_receta, name='vista_nueva_receta'),
    path('receta/edit/<int:id>', views.editar_receta, name='vista_editar_receta'),
]
