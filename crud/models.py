from django.db import models

# Create your models here.
class student(models.Model):
  sid=models.CharField(max_length=4)
  sname=models.CharField(max_length=255)
  scontact=models.CharField(max_length=15)
  
  def __str__(self):
   return self.sname
    
