# Create your views here.

from django.shortcuts import render, render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def viewProfile(request,cui):
    patient = Patient()
    try:
        patient = Patient.objects.get(cui=cui)
        if patient == request.patient:
            return render_to_response('/patient/'+cui)
        except User.DoesNotExist:
            raise Http404
        return render(request)


        

