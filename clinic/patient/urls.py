'''
Created on 21/07/2014

@author: t4r0
'''
from django.conf.urls import patterns, url

from patient import views


urlpatterns = patterns('',
                       url(r'^patient/(?P<cui>\d+)/$',views.viewProfile),
                       
                       #url(r'^signup/$', views.sign_up, name='signup'),
                       )
