from datetime import date, datetime
from django import forms
from django.forms import ModelForm
from .models import Cargos, Empleados


class EmpleadoForm(ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Empleados
        fields = '__all__'
        widgets = {
            "cedula": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            "nombres": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True, 'style': 'text-transform:capitalize;'}),
            "apellidos": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True, 'style': 'text-transform:capitalize;'}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "departamento": forms.Select(attrs={"class": "form-control myselect", "required": True}),
            "ciudad": forms.Select(attrs={"class": "form-control myselect", "id": "ciudademp", "name": "ciudademp", "required": True}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off", 'style': 'text-transform:lowercase;'}),
            "fecha_nto": forms.DateInput(attrs={"class": "form-control", "placeholder": "dd-mm-yyyy"}),
            "cargo": forms.Select(attrs={"class": "form-control"}),
            "inicio_contrato": forms.DateInput(attrs={"class": "form-control", "placeholder": "dd-mm-yyyy"}),
            "fin_contrato": forms.DateInput(attrs={"class": "form-control", "placeholder": "dd-mm-yyyy"}),
        }


class CargosForm(ModelForm):
    class Meta:
        model = Cargos
        fields = '__all__'
        widgets = {
            "cargo": forms.TextInput(attrs={"class": "form-control", "id": "cargo", "name": "cargo", "autocomplete": "off"}),
        }
