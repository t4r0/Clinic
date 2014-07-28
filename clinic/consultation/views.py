# Create your views here.
from djano.views.generic.edit import CreateView
from consultation.models import pathology, consultation, physicaltest
from django.shortcuts import render, render_to_response, Http404
from django.templete import RequestContext
from django.contrib.auth.models import User
from consultation import forms as C_forms


# Librerias usadas para el segundo metodo
from forms import formConsultarion
from django.http import HttpResponseRedirect
from django.core.context_Processors import csrf


# Metodo para obener una consulta existente del sisstema

def view_Consultation(request, idConsulta):
	try:
		consulta = consultation.objects.get(idConsulta = idConsulta)
		examenFisico = physicaltest.objects.filter(idExamenFisico = consulta.Paciente_idPaciente)
		patologia = pathology.objects.filter(idPatologia = consulta.Patologia_idPatologia)

		if request.method == POST:
			form = formConsultarion(request.POST)
			if form.is_valid():
				form.save()




# Metodo para ingresar una nueva consulta al sistema

def consultation_view(request):
	if request.POST:
		form = formConsultarion(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = formConsultarion()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('consulta.html', args)