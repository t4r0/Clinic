'''
Created on 26/07/2014

@author: t4r0
'''
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.http import HttpBadRequest
from django.conf.urls import url
from django.utils.dateparse import parse_date
from appointment.models import appointment as Appointment
class AppointmentResource(ModelResource):
    patient = fields.CharField(readonly=True, attribute='picture', null = True)
    cui = fields.CharField(readonly=True, attribute='picture', null = True)
    class Meta:
        queryset = Appointment.objects.all()
        fields = ['date', 'hour', 'reason']
        authorization = DjangoAuthorization()
        always_return_data = True
        
    def dehydrate_patient(self, bundle):
        return bundle.obj.patient.getfullname()
     
    def dehydrate_cui(self, bundle):
        return unicode(bundle.obj.patient)
    
    def hydrate(self, bundle):
        username = bundle.data['doctor']
        if username:
            try:
                doctor = User.objects.get(username = username)
            except User.DoesNotExist:
                return self.create_response(bundle.request, "Something went wrong",response_class=HttpBadRequest)
            bundle.obj.doctor = doctor.profile
        return bundle
    
    def from_date(self, request, **kwargs):
        if request.user:
            user = request.user
            resource = AppointmentResource()
            appointments = Appointment.objects.filter(doctor=user.profile, date=parse_date(kwargs['date']))
            objects = []
            for appointment in appointments:
                bundle = resource.build_bundle(obj = appointment, request = request)
                bundle = resource.full_dehydrate(bundle)
                objects.append(bundle)
            resource.log_throttled_access(request)
            return self.create_response(request,objects)
        else:
            return self.create_response(request,'Algo anda mal', response_class=HttpBadRequest)
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
        
    def prepend_urls(self):
        return [
                 url(r'^appointment/(?P<pk>\d+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
                 url(r'^appointment/(?P<date>\d{4}-\d{2}-\d{2})/$', self.wrap_view('from_date'), name='get_from_date'),
                ]

        