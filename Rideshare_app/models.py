from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User as User_Auth
# Create your models here.



class Rider(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    venmo = models.CharField(max_length = 30, blank = True, null = True)
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    def __str__(self):
        return self.first_name + " " + self.last_name;


class Driver(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    venmo = models.CharField(max_length = 30, blank = True, null = True)
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    car_make = models.CharField(max_length = 30, blank = True, null = True)
    car_model = models.CharField(max_length = 30, blank = True, null = True)
    #pending_rides = models.OneToManyField(Rider, blank = True)
    def __str__(self):
        return self.first_name + " " + self.last_name;

class User(models.Model):
    user = models.OneToOneField(User_Auth, related_name='user', null = True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    venmo = models.CharField(max_length = 30, blank = True, null = True)
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    driver = models.ForeignKey(Driver, null = True, on_delete = models.CASCADE)
    rider = models.ForeignKey(Rider, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.first_name + " " + self.last_name;


class Ride(models.Model):
    departure_location = models.CharField(max_length = 30)
    destination_location = models.CharField(max_length = 30)
    departure_state = models.CharField(max_length = 30, null = True, blank = True)
    destination_state = models.CharField(max_length = 30, null = True, blank = True)

    date = models.DateField()
    time = models.TimeField(blank = True, null = True)
    seats = models.IntegerField(null = True, blank = True, default=1, validators=[MinValueValidator(1)])
    price = models.IntegerField(null = True, blank = True, default=0, validators=[MinValueValidator(0)])
    # each ride links to only one driver
    driver = models.ForeignKey(Driver, null = True, on_delete = models.CASCADE)
    riders = models.ManyToManyField(Rider, blank = True)
    confirmed_riders = models.ManyToManyField(Rider, blank = True, related_name = "confirmed_riders")
    pending_riders = models.ManyToManyField(Rider, blank = True, related_name = "pending_riders")
