from django.db import models

# Create your models here.
persona_sexo = [("femenimo", "Femenino"), ("masculino", "Masculino")]


class Departamento(models.Model):
    nombre_dep = models.CharField(max_length=50)
    codigo = models.IntegerField()

    def __str__(self):
        return (self.nombre_dep)


class Municipios(models.Model):
    departamento = models.ForeignKey(
        Departamento, verbose_name='ciudad', on_delete=models.CASCADE)
    codigo = models.IntegerField()
    nombre_mun = models.CharField(max_length=100)

    def __str__(self):
        return (self.nombre_mun)


class Cargos(models.Model):
    cargo = models.CharField(
        max_length=50, verbose_name="Cargos", unique="true")

    def __str__(self):
        return (self.cargo)


class Persona(models.Model):
    cedula = models.CharField(
        max_length=10, verbose_name="Cedula", unique="true")
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    direccion = models.CharField(max_length=70, verbose_name="Direccion")
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, max_length=70, null="true", blank="true", verbose_name="Departamento")
    ciudad = models.ForeignKey(
        Municipios, on_delete=models.CASCADE, null="true", blank="true", max_length=70, verbose_name="Ciudad")
    telefono = models.CharField(max_length=12, verbose_name="Telefono")
    sexo = models.CharField(choices=persona_sexo, null="false",
                            blank="false", max_length=12, verbose_name="Sexo")
    email = models.EmailField(verbose_name="Email")
    fecha_nto = models.DateField()

    class Meta:
        abstract = True


class Empleados(Persona):
    cargo = models.ForeignKey(
        Cargos, on_delete=models.CASCADE, max_length=50, verbose_name="Cargos")
    inicio_contrato = models.DateField()
    fin_contrato = models.DateField()
    foto = models.ImageField(upload_to='empleado', null=True, blank=True)

    def __str__(self):
        return (self.cedula)
