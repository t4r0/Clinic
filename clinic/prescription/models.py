from django.db import models
from patient.models import patient
from consultation.models import consultation

# Create your models here.

class medicine(models.Model):
    medicine=models.CharField(max_length=75,blank=False,null=False)

    def __unicode__(self):
        return str(self.medicine)


class prescription(models.Model):
    date = models.DateField()
    observations=models.TextField()
    patient=models.ForeingKey(patient)
    consultation=models.ForeingKey(consultation)
    medicine=models.ForeingKey(medicine)

    
