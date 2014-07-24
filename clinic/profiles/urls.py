'''
Created on 21/07/2014

@author: t4r0
'''
from django.conf.urls import patterns, url

from profiles import views


urlpatterns = patterns('', 
                       url(r'^$', views.main, name='home'),
                         url(r'^Login/', 'django.contrib.auth.views.login',
                            {'template_name':'profiles/login.html'}, name = 'login')
                       )
