from django import forms
from .models import Log, Vehicle
from django.core.exceptions import ValidationError

class LogForm(forms.ModelForm):
    def clean_fuel_type(self):
        vehicle: Vehicle = self.cleaned_data.get('vehicle')
        fuel: str = self.cleaned_data.get('fuel_type')
        valid_fuel_types = {
            'car': ['petrol', 'cng'],
            'bike': ['petrol']
        }
        if fuel not in valid_fuel_types.get(vehicle.vehicle_type, []):
            raise ValidationError(f"{fuel.capitalize()} is not valid for {vehicle.vehicle_type.capitalize()}")
        return fuel
    class Meta:
        model = Log
        fields = ['price', 'quantity', 'vehicle', 'fuel_type', 'odo','location']