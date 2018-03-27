from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Appointment
from .forms import AppointmentForm

def index(request):
	if request.method == 'GET':
		if request.GET.has_key('query'):
			query = request.GET['query']
			q = Q(datetime__contains=query)
			q.add(Q(description__contains=query), Q.OR)
			appointments = Appointment.objects.filter(q).order_by('-datetime')[:100]
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
		
		
