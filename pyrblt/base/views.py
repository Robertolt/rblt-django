from django.shortcuts import render

# Create your views here.
from pyrblt.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
