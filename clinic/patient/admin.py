from django.contrib import admin

# Register your models here.
from models import patient, attendant, status
admin.site.register(patient)
admin.site.register(attendant)
admin.site.register(status)