from django.db import models
from AppSocios.models import Socios
# Create your models here.


class TipoEmbarcacion(models.Model):
    tipo = models.CharField(
        max_length=20, verbose_name="Tipos", unique="true")

    def __str__(self):
        return (self.tipo)


class Embarcacion(models.Model):
    matricula = models.CharField(max_length=10,  unique="true")
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    tipo = models.ForeignKey(
        TipoEmbarcacion, on_delete=models.CASCADE, null="true", blank="true", max_length=20)
    amarre = models.CharField(max_length=5)
    modelo = models.CharField(max_length=12)
    propietario = models.ForeignKey(
        Socios, on_delete=models.CASCADE,  max_length=70)
    foto = models.ImageField(upload_to='embarcacion', null=True, blank=True)

    def __str__(self):
        return (self.matricula)
