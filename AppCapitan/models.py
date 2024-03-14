from django.db import models
from AppEmpleados.models import Persona

# Create your models here.


class Capitan(Persona):
    documentos1 = models.FileField(
        upload_to='documentos', null=True, blank=True)
    documentos2 = models.FileField(
        upload_to='documentos', null=True, blank=True)
    documentos3 = models.FileField(
        upload_to='documentos', null=True, blank=True)
    foto = models.ImageField(upload_to='capitanes', null=True, blank=True)

    def __str__(self):
        return (f"{self.cedula}. {self.nombres} {self.apellidos}")
