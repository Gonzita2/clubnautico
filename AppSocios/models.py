from django.db import models
from AppEmpleados.models import Persona

# Create your models here.


class Profesiones(models.Model):
    profesion = models.CharField(max_length=50, unique="true")

    def __str__(self):
        return (self.profesion)


class Socios(Persona):
    profesion = models.ForeignKey(
        Profesiones, on_delete=models.CASCADE, max_length=50, verbose_name="Profesiones")
    foto = models.ImageField(upload_to='socio', null=True, blank=True)

    def __str__(self):
        return (f"{self.cedula} {self.profesion}. {self.nombres} {self.apellidos}")
