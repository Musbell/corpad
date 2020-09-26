from django import forms
from .models import *

class CreateSchemaForm(forms.ModelForm):
    class Meta:
        model   =   Schema
        fields  =   '__all__'
