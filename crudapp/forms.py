from django import forms
from django.forms import inlineformset_factory

from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'