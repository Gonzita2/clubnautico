from django.urls import path
from .views import consultarEmpleado, crearEmpleado, editarEmpleado, \
    listarEmpleados, crearEmpleadoajax

urlpatterns = [
    path('crearempleado/', crearEmpleado, name='crearempleado'),
    path('editarempleado/<int:id>', editarEmpleado, name='editarempleado'),
    path('consultarempleado/<int:id>',
         consultarEmpleado, name='consultarempleado'),
    path('listarempleados/', listarEmpleados, name='listarempleados'),
    path('crearempleadoajax/<int:id>',
         crearEmpleadoajax, name='crearempleadoajax'),
]
