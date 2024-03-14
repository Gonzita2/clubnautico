from django.urls import path
from .views import crearSocio, crearSocioajax, listarSocio, editarSocio, consultarSocio

urlpatterns = [
    path('crearsocio/', crearSocio, name='crearsocio'),
    path('editarsocio/<int:id>', editarSocio, name='editarsocio'),
    path('consultarsocio/<int:id>',
         consultarSocio, name='consultarsocio'),
    path('listarsocios/', listarSocio, name='listarsocios'),
    path('crearsocioajax/<int:id>',
         crearSocioajax, name='crearsocioajax'),
]
