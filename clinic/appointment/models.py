from django.db import models
from patient.models import patient
from profiles.models import profile
# Create your models here.
class appointment(models.Model):
    patient = models.ForeignKey(patient)
    doctor = models.ForeignKey(profile)
    date = models.DateField()
    hour = models.TimeField(unique_for_date='date')
    reason = models.SlugField(default='consulta de rutina',blank=True)
    
    def __unicode__(self):
        return str(self.date) + str(self.hour)