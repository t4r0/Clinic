# Create your views here.

from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def viewProfile(request,cui):
    user = User()
    try:
        user = User.objects.get(cui=cui)
        if user == request.user:
            return HttpResponseRedirect('/patient/'+cui)
        except User.DoesNotExist:
            raise Http404
        return render(request)


        

