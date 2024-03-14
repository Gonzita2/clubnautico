from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Embarcacion
from .form import EmbarcacionForm

# Create your views here.


@permission_required('AppEmbarcacion.add_embarcacion', login_url="/inicio/")
def crearEmbarcacion(request):
    form = EmbarcacionForm(request.POST or None)
    form1 = EmbarcacionForm(request.POST, request.FILES)
    data = {"form": form, "titulo": "Registrar Embarcacion"}
    if request.method == "POST" or request.method == "FILE":
        if form1.is_valid():
            try:
                form1.save()
                data["mensaje"] = "La Embarcacion fue Registrada con Exito"
                return render(request, "AppEmbarcacion/crearembarcacion.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppEmbarcacion/crearembarcacion.html", data)


@permission_required('AppEmbarcacion.view_embarcacion', login_url="/inicio/")
def listarEmpbarcaciones(request):
    lista = Embarcacion.objects.all()
    data = {"lista": lista, "titulo": "Relacion de  Embarcaciones"}
    return render(request, "AppEmbarcacion/listarembarcaciones.html", data)


@permission_required('AppEmbarcacion.change_embarcacion', login_url="/inicio/")
def editarEmbarcacion(request, matricula):
    obj = Embarcacion.objects.get(matricula=matricula)
    form = EmbarcacionForm(request.POST or None, instance=obj)
    form1 = EmbarcacionForm(request.POST, request.FILES or None, instance=obj)
    data = {"form": form, "titulo": "Editar Embarcacion"}
    if request.method == "POST" or request.method == "FILE":
        if form1.is_valid():
            try:
                form1.save()
                data["mensaje"] = "La Informacion de la Embarcacion fue Actualizada"
                data["myurl"] = "/embarcacion/listarembarcaciones/"
                return render(request, "AppEmbarcacion/editarembarcacion.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppEmbarcacion/editarembarcacion.html", data)


@permission_required('AppEmbarcacion.view_embarcacion', login_url="/inicio/")
def consultarEmbarcacion(request, matricula):
    obj = Embarcacion.objects.get(matricula=matricula)
    form = EmbarcacionForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Consulta de Embarcacion", "imagen": obj.foto}
    return render(request, "AppEmbarcacion/consultarembarcacion.html", data)


@permission_required('AppEmbarcacion.add_embarcacion', login_url="/inicio/")
def crearEmbarcacionajax(request, matricula):
    if request.method == "GET":
        try:
            mimatricula = Embarcacion.objects.filter(
                matricula=matricula).count()
            # print(mimatricula)
            if mimatricula:
                return JsonResponse({"status": 1})
            return JsonResponse({"status": 0})
        except Exception:
            return JsonResponse({"status": 2})
