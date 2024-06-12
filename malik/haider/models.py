from email.headerregistry import Address
from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    taste=models.CharField(max_length=30)
    whatsnew=models.CharField(max_length=30)
    changes=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Home(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    address=models.CharField(max_length=400)
    mainarea=models.CharField(max_length=20)
    subarea=models.IntegerField()
    streetno=models.CharField(max_length=30)
    flavour=models.CharField(max_length=20)
    topping=models.IntegerField()
    instructions=models.CharField(max_length=30)

    def __str__(self):
        return self.name



