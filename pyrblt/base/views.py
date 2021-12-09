from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):   #this always need to have 'request' as parameter
    return HttpResponse('Olá Django')
