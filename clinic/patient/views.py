# Create your views here.

from django.shortcuts import render, render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from patient.models import patien
from consultation.models import consultation

def viewProfile(request,cui):
    try:
        patient = patient()
        consultation = consultation()
        patient = patient.objects.get(cui=cui)
        consultation = consultation.objects.filter(patient=patient).all()        
        if patient == request.patient:
            return render_to_response(request,'/patientProfile.html',{'patient':patient,
                                                                      'consultation':consultation.order_by('-date')[:10],
                                                                      })
        except User.DoesNotExist:
            raise Http404


        

