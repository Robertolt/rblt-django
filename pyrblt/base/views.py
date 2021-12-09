from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.


def home(request):   #this always need to have 'resquest' as parameter
    return HTTPResponse('Olá Django')
