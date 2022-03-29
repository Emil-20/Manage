from django.db import models

# Create your models here.


class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.CharField(max_length=30)
    Messages = models.CharField(max_length=100)


class Enquiry(models.Model):
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Pin = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.CharField(max_length=30)
    Messages = models.CharField(max_length=100)
