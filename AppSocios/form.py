from datetime import date, datetime
from django import forms
from django.forms import ModelForm
from .models import Socios, Profesiones


class SocioForm(ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Socios
        fields = '__all__'
        widgets = {
            "cedula": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            "nombres": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "apellidos": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "departamento": forms.Select(attrs={"class": "form-control myselect", "required": True}),
            "ciudad": forms.Select(attrs={"class": "form-control myselect", "id": "ciudademp", "name": "ciudademp", "required": True}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", }),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off", }),
            "fecha_nto": forms.DateInput(attrs={"class": "form-control", "placeholder": "dd-mm-yyyy"}),
            "profesion": forms.Select(attrs={"class": "form-control", "required": True}),
        }


class ProfesionesForm(ModelForm):
    class Meta:
        model = Profesiones
        fields = '__all__'
        widgets = {
            "profesion": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
        }
