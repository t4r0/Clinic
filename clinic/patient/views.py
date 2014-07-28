# Create your views here.

from django.shortcuts import render, render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from patient.models import patient as Patient
from consultation.models import consultation as Consultation

def viewProfile(request,cui):
    try:
        patient = Patient()
        consultation = Consultation()
        patient = Patient.objects.get(cui=cui)
        consultation = Consultation.objects.filter(patient=patient).all()        
        return render_to_response('patients/patientProfile.html',
                                  {'patient':patient,'consultation':consultation.order_by('-date')[:10]},
                                  context_instance=RequestContext(request))
    except patient.DoesNotExist:
            raise Http404


@login_required        
def addConsultation(request,cui):
    try:
        patient = Patient()
        consultation = Consultation()
        patient = Patient.objects.get(cui=cui)
        consultation = Consultation.objects.filter(patient=patient).all()        
        return render_to_response('patients/consultation.html',
                                  {'patient':patient,'consultation':consultation.order_by('-date')[:10]},
                                  context_instance=RequestContext(request))
    except patient.DoesNotExist:
            raise Http404
