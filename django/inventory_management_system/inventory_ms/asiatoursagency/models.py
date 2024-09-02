from django.db import models

# Create your models here.
class Tour(models.Model):
  # we need country,destination,number of night, price
  origin_country = models.CharField(max_length=64)
  destination_country = models.CharField(max_length=64)
  number_of_night = models.IntegerField()
  price = models.IntegerField()