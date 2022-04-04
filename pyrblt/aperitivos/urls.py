from django.urls import path

from pyrblt.aperitivos.views import video, indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),

]
