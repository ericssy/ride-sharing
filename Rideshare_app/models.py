from django.db import models
from django.forms import ModelForm
import datetime
# Create your models here.

class Rider(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + " " + self.last_name;


class Driver(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    def __str__(self):
        return self.first_name + " " + self.last_name;


class Ride(models.Model):
    departure_location = models.CharField(max_length = 30)
    destination_location = models.CharField(max_length = 30)
    date = models.DateField()
    # each ride links to only one driver
    driver = models.ForeignKey(Driver, null = True, on_delete = models.CASCADE)
    riders = models.ManyToManyField(Rider, blank = True)

class PostRideAsDriverForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['date', "departure_location", "destination_location"]

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(primary_key = True)
    venmo = models.CharField(max_length = 30)
    car_make = models.CharField(max_length = 30)
    car_model = models.CharField(max_length = 30)
    # rides = models.ManyToManyField(Trip)
    # drives = models.ManyToManyField(Trip)

class Trip(models.Model):
    departure_city = models.CharField(max_length = 30)
    departure_state = models.CharField(max_length = 30)
    destination_city = models.CharField(max_length = 30)
    destination_state = models.CharField(max_length = 30)
    date = models.DateField()
    time = models.TimeField()
    driver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "driver")
    seats = models.IntegerField()
    confirmed_riders = models.ManyToManyField(User, related_name = "confirmed_riders")
    pending_riders = models.ManyToManyField(User, related_name = "pending_riders")
