from django.shortcuts import render

from pyrblt.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas=facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})
