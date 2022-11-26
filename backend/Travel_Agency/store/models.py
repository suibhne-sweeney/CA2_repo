from django.db import models
from django.urls import reverse
# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="locations")
    star_rate = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="locations")

    def __str__(self):
        return self.name

class LocationHotel(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)





    

