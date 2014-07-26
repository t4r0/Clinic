'''
Created on 21/07/2014

@author: t4r0
'''
from django.conf.urls import patterns, url

from profiles import views


urlpatterns = patterns('', 
                       url(r'^$', views.main, name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'profiles/login.html'}, name = 'login'),
                       url(r'^(?P<user_name>\w+)/$', views.profile, name='profile'),
                       #url(r'^signup/$', views.sign_up, name='signup'),
                       )
