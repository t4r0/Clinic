from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
import forms
'''
Created on 26/07/2014

@author: t4r0
'''
def main(request):
    user = User()
    user = request.user
    if user.is_authenticated():
        return render(request, 'appointment/schedule.html', {'user':request.user, 'profile':request.user.profile})
    return render(request, 'inicio.html',{})

def sign_up(request):
    if request.POST:
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            return render_to_response('profiles/signUp.html',{'form':form}, context_instance=RequestContext(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')        
    form = forms.SignUpForm()
    return render(request, 'profiles/signup.html',{'form':form})