from django.db import models

# Create your models here.
class Plato(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    price=models.FloatField()
