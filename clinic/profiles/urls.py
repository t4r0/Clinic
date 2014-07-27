'''
Created on 21/07/2014

@author: t4r0
'''
from django.conf.urls import patterns, url
from profiles import views


urlpatterns = patterns('',                      
                       url(r'^(?P<user_name>\w+)/$', views.profile, name='profile'),                       
                       )
