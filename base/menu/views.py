from multiprocessing import context
from unicodedata import name
from django.shortcuts import render 
from numpy import product
from menu.forms import plato_form
from menu.models import Plato

# Create your views here.
def menu(request):
    context = {
        "platos": Plato.objects.all()
    }
    return render(request, 'menu.html', context=context)

def create_plato(request):
    if request.method == "GET":
        form = plato_form
        context = {'form':form}
        return render(request, 'agregar_plato.html', context=context)
    else:
        form = plato_form(request.POST)
        if form.is_valid():
            new_plato = Plato.objects.create(
                name = form.cleaned_data['nombre'],
                price = form.cleaned_data['precio'],
                description = form.cleaned_data['descripcion'],
            )
            context = {'new_plato':new_plato}
            return render(request, 'agregar_plato.html', context=context)

def buscar_plato(request):
    print(request.GET)
    platos = Plato.objects.filter(name__icontains = request.GET['search'])
    context={'platos':platos}
    return render(request, 'buscar_plato.html', context=context)
