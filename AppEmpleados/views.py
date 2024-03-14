from datetime import date
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Empleados
from .form import EmpleadoForm


@permission_required('AppEmpleados.add_empleados', login_url="/inicio/")
def crearEmpleado(request):
    form = EmpleadoForm(request.POST or None)
    data = {"form": form, "titulo": "Registrar Empleado"}
    print(request.POST)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            miempleado = Empleados.objects.filter(
                cedula=request.POST.get("micedula")).count
            if miempleado:
                return JsonResponse({'status': 1})
            return JsonResponse({'status': 0}, status=400)
    else:
        if request.method == "POST":
            if form.is_valid():
                try:
                    form.save()
                    data["mensaje"] = "El Empleado fue Registrado con Exito"
                    return render(request, "AppEmpleados/crearempleado.html", data)
                except Exception:
                    return HttpResponseRedirect("/")
    return render(request, "AppEmpleados/crearempleado.html", data)


@permission_required('AppEmpleados.view_empleados', login_url="/inicio/")
def listarEmpleados(request):
    lista = Empleados.objects.all().order_by("-id")
    data = {"lista": lista, "titulo": "Relacion de  Empleados"}
    return render(request, "AppEmpleados/listarempleados.html", data)


@permission_required('AppEmpleados.update_empleados', login_url="/inicio/")
def editarEmpleado(request, id):
    obj = Empleados.objects.get(id=id)
    form = EmpleadoForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Editar Cargos"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "La Informacion del Empleado fue Actualizada"
                data["myurl"] = "/empleados/listarempleados"
                return render(request, "AppEmpleados/editarempleado.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppEmpleados/editarempleado.html", data)


@permission_required('AppEmpleados.view_empleados', login_url="/inicio/")
def consultarEmpleado(request, id):
    obj = Empleados.objects.get(id=id)
    form = EmpleadoForm(request.POST or None, instance=obj)
    fecha_edad = obj.fecha_nto
    fecha_actual = date.today()
    miedad = fecha_actual.year - fecha_edad.year
    miedad -= ((fecha_actual.month, fecha_actual.day) < (fecha_edad.month,
                                                         fecha_edad.day))
    data = {"form": form, "miedad": miedad, "titulo": "Consulta de Empleado"}
    return render(request, "AppEmpleados/consultarempleado.html", data)


@permission_required('AppEmpleados.add_empleados', login_url="/inicio/")
def crearEmpleadoajax(request, id):
    if request.method == "GET":
        try:
            micedula = Empleados.objects.filter(cedula=id).count()
            if micedula:
                return JsonResponse({"status": 1})
            return JsonResponse({"status": 0})
        except Exception:
            return JsonResponse({"status": 2})
