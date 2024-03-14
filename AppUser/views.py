from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

# Create your views here.


@permission_required('auth.add_user', login_url="/inicio/")
def crearUsuario(request):
    form = UserCreationForm(request.POST or None)
    data = {"titulo": "Formulario Para Creacion de Usuario", "form": form}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "El Usuario Fue Registrado Con Exito"
                return render(request, "AppUser/listarusers.html", data)
            except Exception:
                return HttpResponseRedirect("/")
    return render(request, "AppUser/crearusuario.html", data)


@permission_required('auth.view_user', login_url="/inicio/")
def listarUsers(request):
    usuarios = User.objects.all()
    data = {"titulo": "Listado d e Usuarios", "usuarios": usuarios}
    return render(request, "AppUser/listarusers.html", data)


def miUsuario(request):

    return render(request, "AppUser/minformacion.html", {"titulo": "Informacion de Usuario"})


@permission_required('auth.update_user', login_url="/inicio/")
def cambiarPassword(request):
    # obj = User.objects.get(id=id)
    form = PasswordChangeForm(request.POST or None)
    data = {"titulo": "Cambiar Contraseña", "form": form}
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                data["mensaje"] = "La Contraseña ha sido Actualizada"
                return render(request, "AppUser/cambiarpassword.html/", data)
            except Exception:
                return HttpResponseRedirect("/")
    return render(request, "AppUser/cambiarpassword.html/", data)
