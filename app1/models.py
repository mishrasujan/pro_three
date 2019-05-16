from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=90)
    age = models.IntegerField(default=10, null=False)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    height= models.IntegerField(default=10, null= False)

class School(models.Model):
    subjects = models.CharField(max_length=50)
    teachers = models.CharField(max_length=20)
    duration = models.IntegerField(max_length=10)
