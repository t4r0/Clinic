from django.shortcuts import render
from django.contrib.auth.models import User
'''
Created on 26/07/2014

@author: t4r0
'''
def main(request):
    user = User()
    user = request.user
    if user.is_authenticated():
        return render(request, 'profiles/profile.html', {'user':request.user, 'profile':request.user.profile})
    return render(request, 'inicio.html',{})

def sign_up(request):
    return render(request, 'profiles/signup.html',{})