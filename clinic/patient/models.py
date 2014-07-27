from django.db import models

# Create your models here.

class status(models.Model):
    """
    Clase que almacena el estado civil que puede
    tener una persona
    """

    status = models.CharField(max_length=45,blank=False,unique=True)

    def __unicode__(self):
        return str(self.status)


class attendant(models.Model):
    """
    Clase que almacena los datos de un encargado
    relacionado con un paciente en especifico
    """    
    cui = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=45,blank=False,null=False)
    last_name = models.CharField(max_length=45,blank=False,null=False)
    phone = models.CharField(max_length=45,blank=False,null=False)
    mobile = models.CharField(max_length=45,blank=False,null=False)

    def __unicode__(self):
        return str(self.cui)

    def getfullname(self):
        return str(self.name)+str(self.last_name)

    
class patient(models.Model):
    """
    Clase que alamacena los datos de un paciente
    """
    attendant= models.ForeignKey(attendant,null=True, blank=True)
    status= models.ForeignKey(status, null=True, blank=True) 
    cui = models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=45,blank=True,null=False)
    last_name=models.CharField(max_length=45,blank=True,null=False)
    date_of_birth= models.DateField()
    adress= models.CharField(max_length=80,blank=True,null=False)
    phone= models.CharField(max_length=45,blank=True,null=False)
    gender=models.BooleanField(blank=True)
    email=models.EmailField(blank=True)
   

    def __unicode__(self):
        return str(self.cui)

    def getfullname(self):
        return str(self.name)+str(self.last_name)

    def getattendant(self):
        return str(self.attendant.getfullname)

    def getStatus(self):
        return str(self.status)
