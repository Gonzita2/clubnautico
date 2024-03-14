from django.urls import path
from .views import crearCapitan, editarCapitan, consultarCapitan, listarCapitanes, crearcapitanajax, \
    capitanPdf

urlpatterns = [
    path('crearcapitan/', crearCapitan, name='crearcapitan'),
    path('editarcapitan/<int:id>',
         editarCapitan, name='editarcapitan'),
    path('consultarcapitan/<int:id>',
         consultarCapitan, name='consultarcapitan'),
    path('listarcapitanes/', listarCapitanes, name='listarcapitanes'),
    path('crearcapitanajax/<int:id>',
         crearcapitanajax, name='crearcapitanajax'),
    path('capitanpdf/<int:id>',
         capitanPdf, name='capitanpdf'),
]
