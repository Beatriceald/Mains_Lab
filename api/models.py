from tkinter import CASCADE
from django.conf import settings
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Organization(models.Model):
    client_name = models.ForeignKey(Client, unique=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Biils(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT)
    client_org = models.ForeignKey(Organization, on_delete=models.PROTECT, unique=True)
    number = models.IntegerField(unique=True)
    sum = models.IntegerField()
    date = models.DateField()
    service = models.CharField(max_length=255)
    fraud_score = models.FloatField()
    service_class = models.IntegerField()
    service_name = models.CharField(max_length=50)
