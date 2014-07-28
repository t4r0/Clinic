'''
Created on 21/07/2014

@author: t4r0
'''
from django.conf.urls import patterns, url

from consultation import views


urlpatterns = patterns('',
                       url(r'^(?P<cui>\d+)/$',views.addConsultation),
                       )
