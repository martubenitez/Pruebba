from unicodedata import name
from django.urls import path
from menu.views import menu
from menu.views import menu

urlpatterns = [
    path('', menu, name='menu'),
]
    
