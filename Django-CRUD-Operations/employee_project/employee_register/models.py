from django.db import models

# Create your models here.



class Employee(models.Model):
    fullname = models.CharField(max_length=100,default="")
    emp_code = models.CharField(max_length=3,default="")
    mobile= models.IntegerField(max_length=15,default="")
    image = models.FileField(upload_to='uploaded-images/',blank=True)

    
