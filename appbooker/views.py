from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Appointment
from .forms import AppointmentForm

def index(request):
	form = AppointmentForm()
	return render(request, 'index.html', {'form': form})

@csrf_exempt	
def getappointments(request):
	if request.method == 'POST':
		query = request.POST['query']
		
		q = Q(date__contains=query)
		q.add(Q(time__contains=query), Q.OR)
		q.add(Q(description__contains=query), Q.OR)
		
		appointments = Appointment.objects.filter(q).order_by('-created_at')
		context = {
			'appointments': list(appointments),
		}
		return render(request, 'appointments.html', context)
		
def add(request):
	if request.method == "POST":
		form = AppointmentForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		return HttpResponseRedirect('/')
