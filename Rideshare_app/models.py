from django.db import models
from django.forms import ModelForm
# Create your models here.



class Rider(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
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
    def __str__(self):
        return self.first_name + " " + self.last_name;

class User(models.Model):
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
    seats = models.IntegerField(null = True, blank = True)
    # each ride links to only one driver
    driver = models.ForeignKey(Driver, null = True, on_delete = models.CASCADE)
    riders = models.ManyToManyField(Rider, blank = True)
    confirmed_riders = models.ManyToManyField(Rider, blank = True, related_name = "confirmed_riders")
    pending_riders = models.ManyToManyField(Rider, blank = True, related_name = "pending_riders")

class PostRideAsDriverForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['date', "departure_location", "destination_location"]
