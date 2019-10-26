from django.db import models
from django.forms import ModelForm
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
