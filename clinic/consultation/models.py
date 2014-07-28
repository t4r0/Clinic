from django.db import models
from patient.models import patient
from appointment.models import appointment

# Create your models here.

class pathology(models.Model):
    pathology = models.CharField(max_length=50,blank=False,null=False)

    def __unicode__(self):
        return str(self.pathology)
  
class consultation(models.Model):
    date = models.DateField()
    observation = models.TextField()
    symptoms = models.TextField()
    patient = models.ForeignKey(patient)
    

class physicaltest(models.Model):
    size = models.CharField(max_length=25,blank=False)
    weight = models.FloatField(blank=False)
    pressure = models.CharField(max_length=20,blank=False)
    temperature = models.CharField(max_length=12)
    heartrate = models.CharField(max_length=12)
    consultation = models.ForeignKey(consultation)

class diagnostic(models.Model):
    pathology = models.ForeignKey(pathology)
    consultation = models.ForeignKey(consultation)
