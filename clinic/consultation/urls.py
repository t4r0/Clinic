# Urls para el manejo de consultation

from django.conf.urls import patterns, include, urls

urlpatterns = patterns('', 
	url(r'^consulta/', 'consultation.views.consultation_view', name='consulta'),

	)