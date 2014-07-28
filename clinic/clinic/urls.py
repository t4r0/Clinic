from django.conf.urls import patterns, include, url
from django.contrib import admin
from appointment.resources import AppointmentResource
import views
from tastypie.api import Api
api = Api(api_name='v')
api.register(AppointmentResource())
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),  
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'profiles/login.html'}, name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^$', views.main, name='home'),
    url(r'^patient/', include('patient.urls')),
    url(r'^consultation/', include('consultation.urls')),
    url(r'^', include('profiles.urls'))
    )
