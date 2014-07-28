
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

    def getObservation(self):
        return str(self.observation)

    def getSymptoms(self):
        return str(self.symptoms)
    
    def __unicode__(self):
        return str(self.id)+str(self.date)

class physicaltest(models.Model):
    size = models.CharField(max_length=25,blank=False)
    weight = models.FloatField(blank=False)
    pressure = models.CharField(max_length=20,blank=False)
    temperature = models.CharField(max_length=12)
    heartrate = models.CharField(max_length=12)
    consultation = models.OneToOneField(consultation,related_name='physicaltest')

    def getSize(self):
        return str(self.size)

    def getWeight(self):
        return str(self.weight)

    def getPressure(self):
        return str(self.pressure)
    
    def getHeartRate(self):
        return str(self.heartrate)

    def getTemperature(self):
        return str(self.temperature)

    def __unicode__(self):
        return str(self.id)+str(self.consultation)

class diagnostic(models.Model):
    pathology = models.ForeignKey(pathology)
    consultation = models.OneToOneField(consultation,related_name='diagnostic')

    def getPathology(self):
        return str(self.pathology)

    def __unicode__(self):
        return str(self.id)+str(self.consultation)


