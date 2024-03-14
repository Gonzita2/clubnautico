from django.urls import path
from .views import *


urlpatterns = [
    path('crearusuario/', crearUsuario, name='crearusuario'),
    path('listarusuarios/', listarUsers, name='listarusuarios'),
    path('infousuario/', miUsuario, name='infousuario'),
    path('cambiarpassword/', cambiarPassword, name='cambiarpassword'),
]
