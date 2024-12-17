from django import forms
from .models import Log

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['price', 'quantity', 'fuel_type', 'odo', 'location']