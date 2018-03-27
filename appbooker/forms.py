from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	
    class Meta:
        model = Appointment
        fields = ('date', 'time', 'description',)
        widgets = {
            'date': forms.DateInput(format=('%b %d'), attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
