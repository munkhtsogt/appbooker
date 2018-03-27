from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ('date', 'time', 'description',)
		widgets = {
			'date': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'type': 'date'}),
			'time': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'type': 'time'}),
			'description': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
		}
