from django.shortcuts import render

from menu.models import plato

# Create your views here.
def menu(request):
    context = {
        "platos": plato.objects.all()
    }
    return render(request, 'menu.html', context=context)
