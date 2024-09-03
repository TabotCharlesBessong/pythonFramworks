from django.db import models

# Create your models here.
class Tour(models.Model):
  # we need country,destination,number of night, price
  origin_country = models.CharField(max_length=64)
  destination_country = models.CharField(max_length=64)
  number_of_night = models.IntegerField()
  price = models.IntegerField()
  
  # this is a string representation of the tours
  def __str__(self):
    return (f"ID:{self.id}: From {self.origin_country} - {self.destination_country} for {self.number_of_night} night(s) at ${self.price}")