from django.db import models

class Vegetables(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2000)
