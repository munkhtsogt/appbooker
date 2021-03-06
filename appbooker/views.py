from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import admin

def index(request):
	if request.method == 'GET':
		if request.GET.has_key('query'):
			query = request.GET['query']
			q = Q(datetime__regex=query)
			q.add(Q(desc__contains=query), Q.OR)
			appointments = Appointment.objects.filter(q).order_by('-datetime')
			appointments = serializers.serialize('json', appointments)
			return HttpResponse(appointments, content_type='application/json')
		else:
			form = AppointmentForm()
			return render(request, 'index.html', {'form': form})
	
	else:
		form = AppointmentForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		return HttpResponseRedirect('/')	

# FOR I18N		
def i18n_javascript(request):
	return admin.site.i18n_javascript(request)
