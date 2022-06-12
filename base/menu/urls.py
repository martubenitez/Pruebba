from unicodedata import name
from django.urls import path
from menu.views import menu, create_plato, buscar_plato


urlpatterns = [
    path('', menu, name='menu'),
    path('agregar-plato/', create_plato, name='create_plato'),
    path('buscar-plato/', buscar_plato, name='buscar_plato'),
]
    
