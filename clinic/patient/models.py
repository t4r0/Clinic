from django.db import models

# Create your models here.

class status(models.Model):
    """
    Clase que almacena el estado civil que puede
    tener una persona
    """

    status = models.CharField(max_length=45,blank=False,unique=True)

    def __unicode__(self):
        return self.status


class attendant(models.Model):
    """
    Clase que almacena los datos de un encargado
    relacionado con un paciente en especifico
    """

    cui = models.IntegerField(unique=True)
    name = models.CharField(max_length=45,blank=False,null=False)
    last_name = models.CharField(max_length=45,blank=False,null=False)
    phone = models.CharField(max_length=45,blank=False,null=False)
    mobile = models.CharField(max_length=45,blank=False,null=False)

    def __unicode__(self):
        return self.cui

class patient(models.Model):
    """
    Clase que alamacena los datos de un paciente
    """

    cui = models.IntegerField(unique=True)
    name=models.CharField(max_length=45,blank=False,null=False)
    last_name=models.CharField(max_length=45,blank=False,null=False)
    date_of_birth= models.DateField()
    adress= models.CharField(max_length=80,blank=False,null=False)
    phone= models.CharField(max_length=45,blank=False,null=False)
    gender=models.BooleanField()
    email=models.EmailField()
    attendant= models.OneToOneField(attendant,null=True)
    status= models.ForeignKey(status) 


    def __unicode__(self):
        return self.cui

    
