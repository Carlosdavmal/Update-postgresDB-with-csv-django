from django.db import models
from django.db.models import CharField


# Create your models here.

#class dataset(models.Model):
 #   id_ds=models.IntegerField(primary_key=True)
  #  name_ds=models.CharField(max_length=95)
   # date_ds=models.DateField()

class Row(models.Model):
    
    dataset = models.CharField(max_length=20)
    point = models.CharField(max_length=20)
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=45)

    def __str__(self):
        return  f'{self.client_id}{self.client_name}'