from django.db import models

# Create your models here.
class Ride(models.Model):
    departure_location = models.CharField(max_length = 30)
    destination_location = models.CharField(max_length = 30)
    date = models.DateField()

class Rider(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    ride = models.ForeignKey(Ride, null = True, on_delete=models.SET_NULL)

class Driver(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    ride = models.ForeignKey(Ride, null = True, on_delete=models.SET_NULL)
