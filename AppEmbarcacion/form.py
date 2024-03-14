from datetime import date, datetime
from django import forms
from django.forms import ModelForm
from .models import Embarcacion


class EmbarcacionForm(ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Embarcacion
        fields = '__all__'
        widgets = {
            "matricula": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            "nombres": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "tipo": forms.Select(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "amarre": forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": True}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "propietario": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
