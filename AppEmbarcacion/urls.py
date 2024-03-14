from django.urls import path
from .views import crearEmbarcacion, crearEmbarcacionajax, listarEmpbarcaciones, consultarEmbarcacion, editarEmbarcacion

urlpatterns = [
    path('crearembarcacion/', crearEmbarcacion, name='crearembarcacion'),
    path('editarembarcacion/<str:matricula>',
         editarEmbarcacion, name='editarembarcacion'),
    path('consultarembarcacion/<str:matricula>',
         consultarEmbarcacion, name='consultarembarcacion'),
    path('listarembarcaciones/', listarEmpbarcaciones, name='listarembarcaciones'),
    path('crearembarcacionajax/<str:matricula>',
         crearEmbarcacionajax, name='crearembarcacionajax'),
]
