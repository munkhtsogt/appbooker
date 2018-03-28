from django import forms
from .models import Appointment
from django.contrib.admin import widgets

class AppointmentForm(forms.ModelForm):
	datetime = forms.DateTimeField(label='', widget=widgets.AdminSplitDateTime(attrs={'required': 'true'}))
	
	class Meta:
		model = Appointment
		fields = ['datetime', 'desc']
		widgets = {
			'desc': forms.TextInput(attrs={'required': 'true'})
		}
