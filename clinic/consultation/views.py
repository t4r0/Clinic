# Create your views here.

from django.shortcuts import render, render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from patient.models import patient as Patient


def addConsultation(request, cui):
        try:
                patient = Patient()
                return render_to_response('consultation/addConsultation.html',
                                          {'patient':patient},
                                           context_instance=RequestContext(request))
	
	except patiente.DoesNotExist:
		raise Https404	
	
