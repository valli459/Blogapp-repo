from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    class Meta:
        abstract = True  ##"ContactInfo" is base-model(Abstract-Base-Class)

class Student(ContactInfo):
    rollno = models.IntegerField()
    mark = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()
