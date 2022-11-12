from django import forms
from .models import Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetaForm(forms.ModelForm):
    error_css_class = 'text-red-600'
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'}),
            'preparacion': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'foto': forms.FileInput(attrs={'class': 'block mb-5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'})
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        preparacion = cleaned_data.get('preparacion')
        foto = cleaned_data.get('foto')

        if not nombre:
            self.add_error('nombre', 'El nombre es obligatorio')
        
        if not nombre[0].isupper():
            self.add_error('nombre', 'El nombre debe empezar por mayúscula')

        if not preparacion:
            self.add_error('preparacion', 'La preparación es obligatoria')
        
        if not preparacion[0].isupper():
            self.add_error('preparacion', 'La preparación debe empezar por mayúscula')

        if not foto:
            self.add_error('foto', 'La foto es obligatoria')


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(forms.ModelForm):
    error_css_class = 'text-red-600'
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'}))
    class Meta:
        model = User
        fields = ['username', 'password']