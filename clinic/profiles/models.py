from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    speciality = models.CharField(max_length = 100, null=True, blank=True)
    telephone = models.CharField(max_length = 20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    emergency_phone = models.CharField(max_length=20, null =True, blank=True)
    active = models.BooleanField(default=True,blank=True)
    registration_number=models.CharField(max_length=10, blank=False)
    def __unicode__(self):
        return self.user.username