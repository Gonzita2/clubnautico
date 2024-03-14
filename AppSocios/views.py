from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Socios, Profesiones
from .form import SocioForm, ProfesionesForm

# Create your views here.

"""
def crearProfesion(request):
    form = ProfesionesForm(request.POST or None)
    data = {"form": form, "titulo": "Registrar Cargos"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "1"
                return render(request, "AppEmpleados/crearcargo.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppEmpleados/crearcargo.html", data)


def listarProfesion(request):
    lista = Profesiones.objects.all()
    data = {"lista": lista, "titulo": "Listado de Cargos"}
    return render(request, "AppEmpleados/listarcargos.html", data)


def editarProfesion(request, id):
    obj = Profesiones.objects.get(id=id)
    form = ProfesionesForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Editar Cargo"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "1"
                return render(request, "AppEmpleados/editarcargo.html", data)
            except Exception:
                return HttpResponseRedirect("/")
    return render(request, "AppEmpleados/editarcargo.html", data)
"""


@permission_required('AppSocios.add_socios', login_url="/inicio/")
def crearSocio(request):
    form = SocioForm(request.POST or None)
    data = {"form": form, "titulo": "Registro De Socio"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "El Socio Fue Registrado con Exito"
                return render(request, "AppSocios/crearsocio.html", data)
            except Exception:
                return HttpResponseRedirect("/")
    return render(request, "AppSocios/crearsocio.html", data)


@permission_required('AppSocios.view_socios', login_url="/inicio/")
def listarSocio(request):
    lista = Socios.objects.all()
    data = {"lista": lista, "titulo": "Relacion de  Socios"}
    return render(request, "AppSocios/listarsocios.html", data)


@permission_required('AppSocios.change_socios', login_url="/inicio/")
def editarSocio(request, id):
    obj = Socios.objects.get(id=id)
    form = SocioForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Actualizar Informacion de Socio"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "Informacion de Socio Actualizada"
                data["myurl"] = "/socios/listarsocios"
                return render(request, "AppSocios/editarsocio.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppSocios/editarsocio.html", data)


@permission_required('AppSocios.view_socios', login_url="/inicio/")
def consultarSocio(request, id):
    obj = Socios.objects.get(id=id)
    form = SocioForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Consulta Informacion De Socio"}
    return render(request, "AppSocios/consultarsocio.html", data)


@permission_required('AppSocios.add_socios', login_url="/inicio/")
def crearSocioajax(request, id):
    if request.method == "GET":
        try:
            micedula = Socios.objects.filter(cedula=id).count()
            if micedula:
                return JsonResponse({"status": 1})
            return JsonResponse({"status": 0})
        except Exception:
            return JsonResponse({"status": 2})
