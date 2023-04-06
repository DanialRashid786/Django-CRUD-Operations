from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
        
        