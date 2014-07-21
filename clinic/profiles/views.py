from django.shortcuts import render, render_to_response
from django.template import RequestContext


# Create your views here.
def main(request):
    return render(request, 'inicio.html',{})