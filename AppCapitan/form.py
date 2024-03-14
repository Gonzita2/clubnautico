from datetime import date, datetime
from django import forms
from django.forms import ModelForm
from .models import Capitan


class CapitanForm(ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Capitan
        fields = '__all__'
        widgets = {
            "cedula": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            "nombres": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "apellidos": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "departamento": forms.Select(attrs={"class": "form-control myselect", "required": True}),
            "ciudad": forms.Select(attrs={"class": "form-control myselect", "id": "ciudademp", "name": "ciudademp", "required": True}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "fecha_nto": forms.DateInput(attrs={"class": "form-control", "placeholder": "dd-mm-yyyy"}),
            "documento1": forms.FileInput(attrs={"class": "form-control"}),
            "documento2": forms.FileInput(attrs={"class": "form-control"}),
            "documento3": forms.FileInput(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),

        }
