from django.db import models

# Create your models here.

class Demoinfo(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    depart=models.CharField(max_length=100)
    date=models.DateField()