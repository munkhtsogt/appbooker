from django import forms
from .models import Appointment
from django.contrib.admin import widgets

class AppointmentForm(forms.ModelForm):
	
	datetime = forms.DateTimeField(label='', widget=widgets.AdminSplitDateTime())
	  
	class Meta:
		model = Appointment
		fields = ['datetime', 'description']
		widgets = {
			'description': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
		}
