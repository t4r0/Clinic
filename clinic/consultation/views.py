# Create your views here.

from django.shortcuts import render, render_to_response, Http404
from django.templete import RequestContext
from django.contrib.auth.decorators import login_requiered
from django.contrib.auth.models import User

def viewConsultation(request, DPI):
	patient = Patient()
	try:
		patient = Patient.objects.get(DPI = DPI)
		if patient == resquest.patient:
			return render_to_response('/patient/consultation.html')
	except Patiente.DoesNotExist:
		raise Https404	
	return render (request)