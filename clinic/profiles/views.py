from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.    

@login_required
def profile(request, user_name):
    doctor = User()
    try:
        doctor = User.objects.get(username = user_name)
        if not doctor.profile.active:
            raise Http404
    except User.DoesNotExist:
        raise Http404
    return render_to_response('profiles/profile.html',
                              {'user_data': doctor, 'profile': doctor.profile},
                               context_instance=RequestContext(request))