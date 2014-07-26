from django.shortcuts import render, render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def main(request):
    return render(request, 'inicio.html',{})
    
@login_required
def profile(request, user_name):
    user = User()
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render_to_response('profiles/profile.html',
                              {'user': user, 'profile': user.profile},
                               context_instance=RequestContext(request))