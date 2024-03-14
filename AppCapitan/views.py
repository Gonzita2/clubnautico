from datetime import date
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from .models import Capitan
from .form import CapitanForm

# Create your views here.


def crearCapitan(request):
    form = CapitanForm(request.POST or None)
    form1 = CapitanForm(request.POST, request.FILES)
    data = {"form": form, "titulo": "Registrar Datos de Capitan"}
    if request.method == "POST" or request.method == "FILE":
        if form1.is_valid():
            try:
                form1.save()
                data["mensaje"] = "Los Datos del Capitan Fueron Registrados Con Exito"
                return render(request, "AppCapitan/crearcapitan.html", data)
            except Exception:
                return HttpResponseRedirect("/")

    return render(request, "AppCapitan/crearcapitan.html", data)


def listarCapitanes(request):
    lista = Capitan.objects.all()
    data = {"lista": lista, "titulo": "Listado de Capitanes"}
    return render(request, "AppCapitan/listarcapitanes.html", data)


def editarCapitan(request, id):
    obj = Capitan.objects.get(id=id)
    form = CapitanForm(request.POST or None, instance=obj)
    data = {"form": form, "titulo": "Editar Cargo"}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "La Informacion Fue Actualizada"
                data["myurl"] = "/capitanes/listarcapitanes/"
                return render(request, "AppCapitan/editarcapitan.html", data)
            except Exception:
                return HttpResponseRedirect("/")
    return render(request, "AppCapitan/editarcapitan.html", data)


def consultarCapitan(request, id):
    obj = Capitan.objects.get(id=id)
    form = CapitanForm(request.POST or None, instance=obj)
    fecha_edad = obj.fecha_nto
    fecha_actual = date.today()
    miedad = fecha_actual.year - fecha_edad.year
    miedad -= ((fecha_actual.month, fecha_actual.day) < (fecha_edad.month,
                                                         fecha_edad.day))
    data = {"form": form, "titulo": "Consulta Datos de Capitan",
            "miedad": miedad, "myid": id}
    return render(request, "AppCapitan/consultarcapitan.html", data)


def crearcapitanajax(request, id):
    if request.method == "GET":
        try:
            micedula = Capitan.objects.filter(cedula=id).count()
            if micedula:
                return JsonResponse({"status": 1})
            return JsonResponse({"status": 0})
        except Exception:
            return JsonResponse({"status": 2})


def capitanPdf(request, id):
    obj = Capitan.objects.get(id=id)
    fecha_edad = obj.fecha_nto
    fecha_actual = date.today()
    miedad = fecha_actual.year - fecha_edad.year
    miedad -= ((fecha_actual.month, fecha_actual.day) < (fecha_edad.month,
                                                         fecha_edad.day))
    context = {"form": obj, "miedad": miedad}
    html = render_to_string("AppCapitan/capitanpdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
